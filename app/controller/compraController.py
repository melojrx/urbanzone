import datetime
import locale
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from app.forms.compraForm import CompraForm
from app.models.cartaoCreditoModel import CartaoCredito

from ..database import db
from app.controller.roleRequired import roles_required
from app.models.ticketModel import Ticket
from app.models.compraModel import Compra
from app.rotas.compraRout import compra_bp


class compraController:

   global ROWS_PER_PAGE 
   ROWS_PER_PAGE = 10

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @compra_bp.route('/prepareBuyCard', methods=['GET'])
   def prepareBuyCard():
         
         try:

            form = CompraForm(request.form)
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

            listTicket = Ticket.query.filter( Ticket.datFim.is_(None)).all()
            listCartaoCredito = CartaoCredito.query.filter(CartaoCredito.datFim.is_(None)).all()

            form.quantidade.choices = [(0, "Selecione...e")]+[(row, str(row)) for row in list(range(1, 11))]
            form.cartoes.choices = [(0, "Selecione seu cartão")]+[(row.id, row.txtNumero) for row in listCartaoCredito]
            form.tickets.choices = [(row.id, str(row.txtTicket) + ' - ' +  str(row.horaTicket) + 'H - ' + str(locale.currency(row.valorTicket, grouping=True, symbol=None))) for row in listTicket]

            return render_template('comprarCartao.html', form=form)
            
         except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('comprarCartao.html', form=form)

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @compra_bp.route('/buyCard', methods=['GET'])
   def buyCard():
         
         try:

            form = CompraForm(request.form)

 
            return render_template('comprarCartao.html')
            
         except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('comprarCartao.html')

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @compra_bp.route('/listCompra', methods=['GET'])
   def listCompra():
         
         page = request.args.get('page', 1, type=int)

         try:
            listCompra= db.session.query(Compra).paginate(page=page, per_page=ROWS_PER_PAGE)
            return render_template('listCompra.html', listCompra=listCompra)
            
         except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('listCompra.html', listCompra=listCompra)
