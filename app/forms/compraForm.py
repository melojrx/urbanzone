from wtforms import Form, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired, InputRequired, Length

class CompraForm(Form):

    quantidade = SelectField(
        'Quantidade:',
        coerce=int,
        validators = [
            DataRequired(message='*Campo Requerido'),
            InputRequired(message=('*Campo Requerido'))
    ])

    tickets = RadioField(
        'Tickets:',
        coerce=int,
        validators = [
            DataRequired(message='*Campo Requerido'),
            InputRequired(message=('*Campo Requerido'))
    ])
    
    cartoes = SelectField(
        'Cartão de Crédito:',
        coerce=int,
        validators = [
            DataRequired(message='*Campo Requerido'),
            InputRequired(message=('*Campo Requerido'))
    ]) 

    submit = SubmitField('Estacionar')