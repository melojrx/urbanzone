from app.models.usuarioVeiculoModel import UsuarioVeiculoModel
from ..database import db
import datetime
from app.models.userModel import User
from app.models.veiculoModel import Veiculo
from flask_login import login_required, current_user
from .roleRequired import  roles_required
from ..forms.usuarioVeiculoForm import UsuarioVeiculoForm
from ..rotas.usuarioVeiculorout import usuarioVeiculo_bp
from flask import flash, redirect, render_template, request, url_for, Response, jsonify

class solicitacaoController:

    @login_required
    @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
    @usuarioVeiculo_bp.route('/prepareAdd', methods=['GET'])
    def prepareAdd():
            
            try:
                form =  UsuarioVeiculoForm(request.form)
            except Exception as e:
                flash('Erro: {}'.format(e), 'error') 
                return render_template('addVeiculo.html', form=form)
            
            return render_template('addVeiculo.html', form=form)

    @login_required
    @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
    @usuarioVeiculo_bp.route('/addVeiculo', methods=['GET', 'POST'])
    def addVeiculo():
            try:
                form =  UsuarioVeiculoForm(request.form)

                txtVeiculo = form.veiculo.data
                txtPlaca = form.placa.data
                datInicio = datetime.datetime.now()

                veiculo = Veiculo.query.filter(Veiculo.txtVeiculo == str(txtVeiculo)).first()
                   
                if (veiculo is None):
                    flash('Selecione um veículo na pesquisa por nome de veículo', 'error')
                    return redirect(url_for('usuarioVeiculo.prepareAdd'))
                else:
                    usuarioVeiculo = UsuarioVeiculoModel(current_user.id, veiculo.id, txtPlaca, datInicio)
                    db.session.add(usuarioVeiculo)
                    db.session.commit()
                    flash('Evento cadastrado com sucesso', 'sucess')
                    return redirect(url_for('usuarioVeiculo.prepareAdd'))

            except Exception as e:
                 db.session.rollback()
                 flash('Erro: {}'.format(e), 'error') 
                 return redirect(url_for('usuarioVeiculo.prepareAdd'))
        

    @usuarioVeiculo_bp.route('/veiculoAutocomplete', methods=['GET'])
    def veiculoAutocomplete():
        veiculoSearch = request.args.get('veiculoSearch')
        listVeiculoAutocomplete = Veiculo.query.filter(Veiculo.txtVeiculo.ilike('%' + str(veiculoSearch) + '%')).all()
        results = [row.txtVeiculo for row in listVeiculoAutocomplete]
        return jsonify(results=results) 