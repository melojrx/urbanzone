from ..database import db
from app.models.userModel import User
from app.models.veiculoModel import Veiculo
from flask_login import login_required
from .roleRequired import  roles_required
from ..forms.usuarioVeiculoForm import UsuarioVeiculoForm
from ..rotas.usuarioVeiculorout import usuarioVeiculo_bp
from flask import flash, redirect, render_template, request, url_for, Response, jsonify

class solicitacaoController:

    @login_required
    @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
    @usuarioVeiculo_bp.route('/usuarioVeiculo', methods=['GET'])
    def prepareAdd():
            
            try:
                form =  UsuarioVeiculoForm(request.form)
            except Exception as e:
                flash('Erro: {}'.format(e), 'error') 
                return render_template('addVeiculo.html', form=form)
            
            return render_template('addVeiculo.html', form=form)

    @login_required
    @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
    @usuarioVeiculo_bp.route('/usuarioVeiculo', methods=['GET'])
    def addVeiculo():
            return render_template('addVeiculo.html')
        

    @usuarioVeiculo_bp.route('/usuarioVeiculo', methods=['GET'])
    def veiculoAutocomplete():
        print('aaaaaa')
        veiculoSearch = request.args.get('veiculoSearch')
        listVeiculoAutocomplete = Veiculo.query.filter(User.name.ilike('%' + str(veiculoSearch) + '%')).all()
        results = [row.txtVeiculo for row in listVeiculoAutocomplete]
        return jsonify(results=results) 