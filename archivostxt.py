f=open('alumnos.txt','r')

# alumnos=f.read()
# print(alumnos)
# f.seek(0) este es para poner el cursor en en esa parte del texto .seek(20)
# alumnos2=f.read() este es para leer los datos del archivo de texto
# print(alumnos2)

alumnos=f.readlines()#imprime todas las lineas
# alumnos=f.readlines()#aqui solo imprime el primero de la liena
palabra="angel"
for n in range(0,len(alumnos)):
    if palabra in alumnos[n]:
        print("hola")
        break
    else:
        print(alumnos)
# print(alumnos[0])
# for item in alumnos:
#     print(item,end='') el end de aqui es para indicarle que no haga salto de linea

# f.write('\n'+'Hola mundo!!!!')
# f.write('\n'+'Nuevo hola mundo!!!!')
f.close()
