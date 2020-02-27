from wtforms import Form, StringField, TextField
from wtforms.fields.html5 import EmailField

from wtforms import validators

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio')

class CommentForm(Form):
    username = StringField('username',
                           [
                               validators.Required(message='El username es requerido'),
                               validators.length(min=4, max=25, message='Ingrese username valido'),
                           ]
                           ),
    email = EmailField('email',
                        [
                               validators.Required(message='El email es requerido'),
                               validators.length(min=4, max=25, message='Ingrese email valido'),
                        ]),
    comment = TextField('Comentario')
    honeypot = TextField('', [length_honeypot])