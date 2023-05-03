from wtforms import Form, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length
 
class EstacionamentoForm(Form):

    veiculos = SelectField(
        'Veículos',
        coerce=int,
        validators = [
            DataRequired(message='*Campo Requerido'),
            InputRequired(message=('*Campo Requerido'))
    ])

    submit = SubmitField('Estacionar')