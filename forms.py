from wtforms import Form
from wtforms import StringField, IntegerField, SelectMultipleField
from wtforms import validators
from wtforms.widgets import ListWidget, CheckboxInput

class CinepolisForm(Form):
    nombre = StringField('Nombre completo', [
        validators.DataRequired(message="Campo requerido")
    ])

    cant_compradores = IntegerField('Cantidad Compradores', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message='Debe haber al menos 1 comprador')
    ])

    cant_boletas = IntegerField('Cantidad de Boletas', [
        validators.DataRequired(message='Campo requerido'),
        validators.NumberRange(min=1, message='Debe comprar al menos 1 boleta')
    ])

    tarjeta = SelectMultipleField(
        'Tarjeta Cineco',
        choices=[('Si', 'Si'), ('No', 'No')],
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False)
    )

