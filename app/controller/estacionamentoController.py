from operator import and_
from flask import flash, render_template, request
from flask_login import current_user, login_required

from app.controller.roleRequired import roles_required
from app.forms.estacionamentoForm import EstacionamentoForm
from app.models.usuarioVeiculoModel import UsuarioVeiculo
from app.rotas.estacionamentoRout import estacionamento_bp


class estacionamentoController:

    @login_required
    @roles_required('URBANMOB_ADMIN, URBANMOB_GOVERNO')
    @estacionamento_bp.route('/preparePark', methods=['GET'])
    def preparePark():
            
            try:
                form =  EstacionamentoForm(request.form)
                listUsuarioVeiculos = UsuarioVeiculo.query.filter(and_(UsuarioVeiculo.idUsuario == current_user.id , UsuarioVeiculo.datFim.is_(None))).all()
                form.veiculos.choices = [(0, "Selecione...")]+[(uve.id, uve.veiculo.txtVeiculo) for uve in listUsuarioVeiculos]
                return render_template('estacionamento.html', form=form)
            except Exception as e:
                flash('Erro: {}'.format(e), 'error') 
                return render_template('estacionamento.html', form=form)