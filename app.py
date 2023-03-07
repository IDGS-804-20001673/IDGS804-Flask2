from flask import Flask, render_template
from flask import request 
import forms 
from flask_wtf.csrf import CSRFProtect
from collections import Counter
from flask import make_response
from flask import flash
import json




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





@app.route("/cajas", methods=['GET','POST'])
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

@app.route("/", methods=['GET','POST'])
def resistencias():
    traduc=forms.TraductForm(request.form)
    valor=""
    resultadoma=""
    resultadomi=""
    banda1=""
    banda2=""
    banda3=""
    banda4=""
    bandas=[]
    colores=""
    resultado=""
    if request.method == 'POST':
        banda1=request.form.get("color1")
        banda2=request.form.get("color2")
        banda3=request.form.get("color3")
        banda4=request.form.get("color4")

        valores = {'negro': 0, 'cafe': 1, 'rojo': 2, 'naranja': 3, 'amarillo': 4,
               'verde': 5, 'azul': 6, 'violeta': 7, 'gris': 8, 'blanco': 9}
        multiplicadores = {'negro': 1, 'cafe': 10, 'rojo': 100, 'naranja': 1000,
                       'amarillo': 10000, 'verde': 100000, 'azul': 1000000,
                       'violeta': 10000000, 'gris': 100000000, 'blanco': 1000000000}
        tolerancias = {'oro': .05, 'plata': .10}
    
        bandas=[banda1,banda2,banda3,banda4]

        valor=str(valores[bandas[0]])+str(valores[bandas[1]])
        resultado=int(valor)*multiplicadores[bandas[2]]
        tolerancia=resultado*tolerancias[bandas[3]]
        resultadoma=resultado+tolerancia
        resultadomi=resultado-tolerancia

        colores = {
    "negro": "black",
    "cafe": "brown",
    "rojo": "red",
    "naranja": "orange",
    "amarillo": "yellow",
    "verde": "green",
    "azul": "blue",
    "violeta": "purple",
    "gris": "gray",
    "blanco": "white",
    "oro": "gold",
    "plata": "silver"
}
    with open("valores.json", 'r') as f:
        data = json.load(f)

    if isinstance(data, list):
        data.append({'valor': str(resultado), 
            'min': str(resultadomi), 
            'max': str(resultadoma), 
            'color1': banda1, 
            'color2': banda2, 
            'color3': banda3})
    else:
        data = [{'valor': str(resultado), 
            'min': str(resultadomi), 
            'max': str(resultadoma), 
            'color1': banda1, 
            'color2': banda2, 
            'color3': banda3}]

    with open("valores.json", 'w') as f:
        json.dump(data, f)
        
    return render_template("resistencias.html",data=data,colores=colores,resultadoma=resultadoma,resultadomi=resultadomi,resultado=resultado,form=traduc,bandas=bandas,banda1=banda1,banda2=banda2,banda3=banda3,banda4=banda4)

@app.route("/resultados", methods=['GET','POST'])
def resultados():
    reg_alum=forms.UserForm(request.form)
    with open("valores.json", 'r') as f:
        data = json.load(f)

    return render_template("resultados.html",data=data,form=reg_alum)

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)