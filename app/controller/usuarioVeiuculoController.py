from app.models.usuarioVeiculoModel import UsuarioVeiculo
from ..database import db
import datetime
from operator import and_
from app.models.veiculoModel import Veiculo
from flask_login import login_required, current_user
from .roleRequired import  roles_required
from ..forms.usuarioVeiculoForm import UsuarioVeiculoForm
from ..rotas.usuarioVeiculoRout import usuarioVeiculo_bp
from flask import flash, redirect, render_template, request, url_for, jsonify

class solicitacaoController:

    @login_required
    @roles_required('URBANZON_USER')
    @usuarioVeiculo_bp.route('/listVeiculo', methods=['GET'])
    def listVeiculo():
           
        try:
            listUsuarioVeiculo = UsuarioVeiculo.query.filter(and_(UsuarioVeiculo.idUsuario == current_user.id, UsuarioVeiculo.datFim.is_(None))).all()
            return render_template('listUsuarioVeiculo.html', listUsuarioVeiculo=listUsuarioVeiculo)
            
        except Exception as e:
            flash('Erro: {}'.format(e), 'error') 
            return render_template('listUsuarioVeiculo.html', listUsuarioVeiculo=listUsuarioVeiculo)

    @login_required
    @roles_required('URBANZON_USER')
    @usuarioVeiculo_bp.route('/prepareAddVeiculo', methods=['GET'])
    def prepareAddVeiculo():
            
            try:
                form =  UsuarioVeiculoForm(request.form)
            except Exception as e:
                flash('Erro: {}'.format(e), 'error') 
                return render_template('addVeiculo.html', form=form)
            
            return render_template('addVeiculo.html', form=form)

    @login_required
    @roles_required('URBANZON_USER')
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
                    return redirect(url_for('usuarioVeiculo.prepareAddVeiculo'))
                else:
                    txtPlaca = txtPlaca.upper() if txtPlaca and txtPlaca != "" else txtPlaca
                    print(txtPlaca)
                    usuarioVeiculo = UsuarioVeiculo(current_user.id, veiculo.id, txtPlaca, datInicio)
                    db.session.add(usuarioVeiculo)
                    db.session.commit()
                    flash('Veículo cadastrado com sucesso', 'sucess')
                    return redirect(url_for('usuarioVeiculo.prepareAddVeiculo'))

            except Exception as e:
                 db.session.rollback()
                 flash('Erro: {}'.format(e), 'error') 
                 return redirect(url_for('usuarioVeiculo.prepareAddVeiculo'))
        

    @usuarioVeiculo_bp.route('/veiculoAutocomplete', methods=['GET'])
    def veiculoAutocomplete():
        veiculoSearch = request.args.get('veiculoSearch')
        listVeiculoAutocomplete = Veiculo.query.filter(Veiculo.txtVeiculo.ilike('%' + str(veiculoSearch) + '%')).all()
        results = [row.txtVeiculo for row in listVeiculoAutocomplete]
        return jsonify(results=results) 
   

    @login_required
    @roles_required('URBANZON_USER')
    @usuarioVeiculo_bp.route('/deleteVeiculo/<idVeiculo>', methods=['GET'])
    def deleteVeiculo(idVeiculo):

            try:
                  datFim = datetime.datetime.now()
                  UsuarioVeiculo.query.filter(UsuarioVeiculo.id==idVeiculo).update({'datFim': datFim})
                  db.session.commit()
                  flash('Veículo excluído com sucesso', 'sucess')
                  return redirect(url_for('usuarioVeiculo.listVeiculo'))
            except Exception as e:
                  db.session.rollback();
                  flash('Erro: {}'.format(e), 'error')
                  return redirect(url_for('usuarioVeiculo.listVeiculo'))     