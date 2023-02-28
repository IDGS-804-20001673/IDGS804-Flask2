f=open('alumnos.txt','r')

# alumnos=f.read()
# print(alumnos)
# f.seek(0) este es para poner el cursor en en esa parte del texto .seek(20)
# alumnos2=f.read() este es para leer los datos del archivo de texto
# print(alumnos2)

alumnos=f.readlines()#imprime todas las lineas
# alumnos=f.readlines()#aqui solo imprime el primero de la liena
palabra="emiliano"
for n in range(0,len(alumnos)):
    pal=alumnos[n]
    if n == len(alumnos)-1:
        if palabra == pal:
            res="sista1"
            break
        else:
            res="no esta1"
    else:
        if palabra == pal[:-1]:
            res="sista2"
            break
        else:
            res="noesta2"

print(res)
# print(alumnos[0])
# for item in alumnos:
#     print(item,end='') el end de aqui es para indicarle que no haga salto de linea

# f.write('\n'+'Hola mundo!!!!')
# f.write('\n'+'Nuevo hola mundo!!!!')
f.close()
