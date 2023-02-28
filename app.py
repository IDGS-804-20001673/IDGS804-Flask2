from flask import Flask, render_template
from flask import request 
import forms 
from flask_wtf.csrf import CSRFProtect
from collections import Counter
from flask import make_response
from flask import flash




app=Flask(__name__)
app.config['SECRET_KEY']="esta es una clave encriptada"
csrf=CSRFProtect()
csrf.init_app(app)

@app.route("/formprueba")
def formprueba():

    return render_template("formprueba.html")


@app.route("/Alumnos", methods=['GET','POST'])
def Alumnos():
    reg_alum=forms.UserForm(request.form)
    datos=list()
    if request.method == 'POST' and reg_alum.validate():
        datos.append(reg_alum.matricula.data)
        datos.append(reg_alum.nombre.data)
        print(reg_alum.matricula.data)
        print(reg_alum.nombre.data)

    return render_template("Alumnos.html",form=reg_alum, datos=datos)





@app.route("/", methods=['GET','POST'])
def cajasDinamicas():
    reg_alum=forms.UserForm(request.form)
    if request.method == 'POST':
        numero=int(reg_alum.numero.data)
        return render_template("cajasDinamicas.html",numero=numero,form=reg_alum)
    else:
        return render_template("cajasDinamicas.html",form=reg_alum)




@app.route("/calculos", methods=['GET','POST'])
def calculos():
    reg_alum=forms.UserForm(request.form)
    lis= request.form.getlist("txtnum")

    maxim = int(lis[0])
    for x in lis:
        if int(maxim) > int(x):
            maxim = maxim
        else:
            maxim=x
   
    minimo = int(lis[0])
    for m in lis:
        if int(minimo) < int(m):
            minimo = minimo
        else:
            minimo=m
    suma=0
    for valor in lis:
        suma = suma + int(valor)
    cant = len(lis)
    promedio = suma / cant

    conteo=Counter(lis)
    resultado={}
    for n in conteo:  
        val=conteo[n]
        resultado[n] = val
    
    return render_template("calculos.html",lis=lis, maxim=maxim, minimo=minimo,promedio=promedio, resultado=resultado)
    

@app.route("/traductor", methods=['GET','POST'])
def traductor():
    traduc=forms.TraductForm(request.form)
    if request.method == 'POST':
        if traduc.espanol.data != None:
            f=open('traducciones.txt','a')
            f.write('\n' + traduc.espanol.data.lower())
            f.write('\n' + traduc.ingles.data.lower())

    traducion=request.form.get("txttraduc")
    palabra=request.form.get("txtPalabra")
    palabra=str(palabra).lower()
    respuesta = " "
    r=open('traducciones.txt','r')
    if palabra != None:
        words=r.readlines()
        if traducion == 'i':
           for n in range(0,len(words)):
                palabra2=words[n]
                if n == len(words)-1:
                    if palabra == palabra2:
                        respuesta=words[n+1]
                        break
                    else:
                        respuesta="No hay traduccion"
                else:
                    if palabra == palabra2[:-1]:
                        respuesta=words[n+1]
                        break
                    else:
                        respuesta="No hay traduccion"
        else:
            for n in range(0,len(words)):
                palabra2=words[n]
                if n == len(words)-1:
                    if palabra == palabra2:
                        respuesta=words[n-1]
                        break
                    else:
                        respuesta="No hay traduccion"
                else:
                    if palabra == palabra2[:-1]:
                        respuesta=words[n-1]
                        break
                    else:
                        respuesta="No hay traduccion"


    return render_template("traductor.html",form=traduc,respuesta=respuesta,palabra=palabra)


@app.route("/cookie", methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)
    response=make_response(render_template('cookie.html',form=reg_user))

    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        password=reg_user.password.data
        datos=user+'@'+password
        success_message='Bienvenido {}'.format(user)
        response.set_cookie('datos_usuario',datos)
        flash(success_message)
    return response

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)