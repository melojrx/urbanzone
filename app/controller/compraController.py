import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from ..database import db
from app.controller.roleRequired import roles_required
from app.models.compraModel import Compra
from app.rotas.compraRout import compra_bp


class compraController:

   global ROWS_PER_PAGE 
   ROWS_PER_PAGE = 10

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
