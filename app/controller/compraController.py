import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from operator import and_

from app.forms.compraForm import CompraForm
from app.models.cartaoCreditoModel import CartaoCredito

from ..database import db
from app.controller.roleRequired import roles_required
from app.models.ticketModel import Ticket
from app.models.compraModel import Compra
from app.rotas.compraRout import compra_bp
from app.utils.currencyUtils import CurrencyUtils


class compraController:

   global ROWS_PER_PAGE 
   ROWS_PER_PAGE = 10

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @compra_bp.route('/prepareBuyCard', methods=['GET'])
   def prepareBuyCard():
         
         try:

            form = CompraForm(request.form)
            

            listTicket = Ticket.query.filter( Ticket.datFim.is_(None)).all()
            listCartaoCredito = CartaoCredito.query.filter(and_(CartaoCredito.idUsuario == current_user.id , CartaoCredito.datFim.is_(None))).all()

            form.quantidade.choices = [(0, "Selecione...")]+[(row, str(row)) for row in list(range(1, 11))]
            form.cartoes.choices = [(0, "Selecione seu cartão")]+[(row.id, row.txtNumero) for row in listCartaoCredito]
            #form.tickets.choices = [(row.id, str(row.txtTicket) + ' - ' +  str(row.horaTicket) + 'H - ' + CurrencyUtils.getStringValue(row.valorTicket)) for row in listTicket]
            form.tickets.choices = [(row.id, str(row.txtTicket) + ' - ' +  str(row.horaTicket) + 'H - ' + str(row.valorTicket)) for row in listTicket]
            return render_template('comprarCartao.html', form=form)
            
         except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('comprarCartao.html', form=form)

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @compra_bp.route('/buyCard', methods=['GET','POST'])
   def buyCard():
         
         try:

            form = CompraForm(request.form)

            idCartao = form.cartoes.data
            idTicket = form.tickets.data
            quantidade = form.quantidade.data
            datInicio = datetime.datetime.now()
 
            compra = Compra(idCartao, idTicket, quantidade, datInicio)
            db.session.add(compra)
            db.session.commit()

            flash('Crédito comprado com sucesso', 'sucess') 
            return redirect(url_for('estacionamento.preparePark'))
            
         except Exception as e:
               db.session.rollback()
               flash('Erro: {}'.format(e), 'error') 
               return render_template('comprarCartao.html')

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @compra_bp.route('/listCompra', methods=['GET'])
   def listCompra():
         
         page = request.args.get('page', 1, type=int)

         try:
            listCompra= Compra.query.join(CartaoCredito).filter(CartaoCredito.idUsuario == current_user.id).paginate(page=page, per_page=ROWS_PER_PAGE)
            return render_template('listCompra.html', listCompra=listCompra)
            
         except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('listCompra.html', listCompra=listCompra)
