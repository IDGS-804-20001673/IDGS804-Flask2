from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField
from wtforms.fields import EmailField, TextAreaField, PasswordField,  RadioField
from wtforms import validators


def mi_validacion(form,field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula=StringField('Matricula',
    [validators.DataRequired('El campo Matricula es requerido'),
    validators.length(min=5,max=10,message='Ingresa min 5 max 10')])
    nombre=StringField('nombre',[validators.DataRequired('El campo nombre es requerido')])
    apaterno=StringField('Apaterno',[mi_validacion])
    amaterno=StringField('Amaterno')
    email=EmailField('correo')
    numero=StringField('Numero')

class TraductForm(Form):
    espanol = StringField('Español')
    ingles = StringField('Ingles')

class LoginForm(Form):
    username=StringField('Usuario',
    [validators.DataRequired('El campo del usuario es requerido'),
    validators.length(min=5,max=10,message='Ingresa min 5 max 10')])

    password=StringField('Contraseña',
    [validators.DataRequired('El campo contraseña es requerido'),
    validators.length(min=5,max=10,message='Ingresa min 5 max 10')])
    


    

     
        
        





