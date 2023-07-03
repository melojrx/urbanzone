from operator import and_
import datetime
from flask import flash, render_template, request, session
from flask_login import current_user, login_required

from ..database import db
from app.controller.roleRequired import roles_required
from app.forms.estacionamentoForm import EstacionamentoForm
from app.models.usuarioVeiculoModel import UsuarioVeiculo
from app.models.cartaoCreditoModel import CartaoCredito
from app.models.compraModel import Compra
from app.models.estacionamentoModel import Estacionamento
from app.models.ticketModel import Ticket
from app.rotas.estacionamentoRout import estacionamento_bp
from app.utils.currencyUtils import CurrencyUtils


class estacionamentoController:

    @login_required
    @roles_required('URBANZON_USER')
    @estacionamento_bp.route('/preparePark', methods=['GET'])
    def preparePark():
            
            try:
                form =  EstacionamentoForm(request.form)

                listUsuarioVeiculos = UsuarioVeiculo.query.filter(and_(UsuarioVeiculo.idUsuario == current_user.id , UsuarioVeiculo.datFim.is_(None))).all()
                listCartaoCredito = CartaoCredito.query.filter(and_(CartaoCredito.idUsuario == current_user.id , CartaoCredito.datFim.is_(None))).all()
                listTicket = Ticket.query.filter(Ticket.datFim.is_(None)).all()
                # LEFT JOIN NESSE SQLALCHEMY FRACO
                listCompras = Compra.query.join(CartaoCredito).outerjoin(Estacionamento, Compra.id == Estacionamento.idCompra).filter(and_(CartaoCredito.idUsuario == current_user.id, Estacionamento.id.is_(None))).all()

                # print('LEFTLEFTLEFTLEFTLEFTLEFTLEFTLEFT', sum([row.ticket.valorTicket for row in listCompras]))

                session["creditos"] = CurrencyUtils.getStringValue(sum([row.ticket.valorTicket for row in listCompras]))
                

                form.veiculos.choices = [(0, "Selecione...")]+[(row.id, row.veiculo.txtVeiculo) for row in listUsuarioVeiculos]
                form.cartoes.choices = [(0, "Selecione seu cartão")]+[(row.id, row.txtNumero) for row in listCartaoCredito]
                form.tickets.choices = [(0, "Selecione o tipo de Ticket")] + [(row.id,"{0} - {1} Hora - R$ {2:,.2f}".format(row.txtTicket, row.horaTicket, row.valorTicket).replace(".", ",")) for row in listTicket]
                #form.tickets.choices = [(0, "Selecione o tipo de Ticket")]+[(row.id, str(row.txtTicket) + ' - ' + str(row.horaTicket) + ' Hora - R$' + str(row.valorTicket) + ',00') for row in listTicket]
                form.quantidade.choices = [(0, "Selecione a quantidade")]+[(row, str(row)) for row in list(range(1, 6))]

                return render_template('estacionamento.html', form=form)
            except Exception as e:
                flash('Erro: {}'.format(e), 'error') 
                return render_template('estacionamento.html', form=form)
            
    @login_required
    @roles_required('URBANZON_USER')
    @estacionamento_bp.route('/addPark', methods=['GET', 'POST'])
    def addPark():
            
            try:
                form =  EstacionamentoForm(request.form)
      
                usuarioVeiculo = form.veiculos.data
                cartao = form.cartoes.data
                ticket = form.tickets.data
                quantidade = form.quantidade.data
                datInicio = datetime.datetime.now()

                compra = Compra(None, ticket, quantidade, datInicio)
                # compra = Compra(cartao, ticket, quantidade, datInicio)
                estacionamento = Estacionamento(usuarioVeiculo, compra, datInicio)

                ticketObj = Ticket.query.filter(Ticket.id == ticket).first()
                tempo = (ticketObj.horaTicket * quantidade) * 3600

                db.session.add(estacionamento)
                db.session.commit()

                #flash('Estacionamento Realizado com sucesso', 'sucess') 
                return render_template('acompanharEstacionamento.html', estacionamento=estacionamento, tempo=tempo)
            except Exception as e:
                db.session.rollback()
                flash('Erro: {}'.format(e), 'error') 
                return render_template('estacionamento.html', form=form)            