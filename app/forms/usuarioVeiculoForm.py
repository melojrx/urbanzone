from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length
 
class UsuarioVeiculoForm(Form):

    veiculo = StringField(
    'Veículo:',
    render_kw={"placeholder": "pesquise por veículos."},
    validators = [
        DataRequired(message='*Campo Requerido'),
        InputRequired(message=('*Campo Requerido'))
    ])

    placa = StringField(
    'Placa:',
    render_kw={"placeholder": "Informe a placa do veículo."},
    validators = [
        DataRequired(message='*Campo Requerido'),
        InputRequired(message=('*Campo Requerido')),
        Length(max=7, message='A placa deve conter %(max)d caracteres.')
    ])

    submit = SubmitField('Cadastrar')