import datetime
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from operator import and_

from ..database import db
from app.controller.roleRequired import roles_required
from app.rotas.cartaoCreditoRout import cartaoCredito_bp
from ..forms.cartaoCreditoForm import CartaoCreditoForm
from ..models.cartaoCreditoModel import CartaoCredito


class cartaoCreditoController:

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @cartaoCredito_bp.route('/listCard', methods=['GET'])
   def listCard():
           
           try:
              listCartaoCredito = CartaoCredito.query.filter(and_(CartaoCredito.idUsuario == current_user.id , CartaoCredito.datFim.is_(None))).all()
              return render_template('listCartaoCredito.html', listCartaoCredito=listCartaoCredito)
            
           except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('listCartaoCredito.html', listCartaoCredito=listCartaoCredito)

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @cartaoCredito_bp.route('/prepareAddCard', methods=['GET'])
   def prepareAddCard():
            
           form =  CartaoCreditoForm(request.form)
           try:
              current_year = datetime.datetime.now().year
              year_list = list(range(current_year-10, current_year+11))
              month_list = list(range(1, 13))
              form.ano.choices = [(0, "Selecione...")]+[(str(year), str(year)) for year in year_list]
              form.mes.choices = [(0, "Selecione...")]+[(str(month), str(month)) for month in month_list]
              return render_template('addCartaoCredito.html', form=form)
            
           except Exception as e:
               flash('Erro: {}'.format(e), 'error') 
               return render_template('addCartaoCredito.html', form=form)
            
   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @cartaoCredito_bp.route('/addCard', methods=['GET', 'POST'])
   def addCard():
            
           form =  CartaoCreditoForm(request.form)
           try:
                 
              txtNumero = form.numero.data;
              txtNome = form.nome.data;
              txtMes = form.mes.data;
              txtAno = form.ano.data;
              txtCVC = form.cvc.data;
              datInicio = datetime.datetime.now()
            
              cartaoCredito = CartaoCredito(current_user.id, txtNumero, txtNome, str(txtMes) + '/' + str(txtAno), txtCVC, datInicio)
              db.session.add(cartaoCredito)
              db.session.commit()

              flash('Cartão de Crédito cadastrado com sucesso', 'sucess')
              return redirect(url_for('cartaoCredito.listCard'))
            
           except Exception as e:
               db.session.rollback();
               flash('Erro: {}'.format(e), 'error') 
               return render_template('addCartaoCredito.html', form=form)

   @login_required
   @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
   @cartaoCredito_bp.route('/deleteCreditCard/<idCartaoCredito>', methods=['GET'])
   def deleteCreditCard(idCartaoCredito):

            try:
                  datFim = datetime.datetime.now()
                  CartaoCredito.query.filter(CartaoCredito.id==idCartaoCredito).update({'datFim': datFim})
                  db.session.commit()
                  flash('Cartão de Crédito excluído com sucesso', 'sucess')
                  return redirect(url_for('cartaoCredito.listCard'))
            except Exception as e:
                  db.session.rollback();
                  flash('Erro: {}'.format(e), 'error')
                  return redirect(url_for('cartaoCredito.listCard'))               