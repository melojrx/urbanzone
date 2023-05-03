from wtforms import Form, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length
 
class CartaoCreditoForm(Form):

    numero = StringField(
        'Número:',
        render_kw={"placeholder": "Informe o número do cartão de crédito."},
        validators = [
            InputRequired(message=('*Campo Requerido')),
            Length(max=16, message='A número deve conter %(max)d caracteres')
        ])
    
    nome = StringField(
        'Nome:',
        render_kw={"placeholder": "Informe o nome igual consta no cartão."},
        validators = [
            InputRequired(message=('*Campo Requerido'))
        ])    

    mes = SelectField(
        'Mês:',
        coerce=int,
        # choices=['01', '02', '03' , '04', '05' , '06', '07', '08', '09', '10', '11', '12'],
        validators = [
            DataRequired(message='*Campo Requerido'),
            InputRequired(message=('*Campo Requerido'))
    ])

    ano = SelectField(
        'Ano:',
        coerce=int,
        validators = [
            DataRequired(message='*Campo Requerido'),
            InputRequired(message=('*Campo Requerido'))
    ])    

    cvc = StringField(
        'CVC:',
        render_kw={"placeholder": "Informe o CVC do cartão de crédito."},
        validators = [
            InputRequired(message=('*Campo Requerido')),
            Length(max=3, message='A número deve conter %(max)d caracteres')
        ])

    submit = SubmitField('Cadastrar')