#Andrea Llavel
from ManejoArchivos import ManejoArchivos
#Manejo de Contexto with:sintaxis simplificada, abre y cierra el archivo
#with open('prueba.txt', 'r', encoding='utf8') as archivo:
    #La ventaja de with es que abre el archivo, pero tambien lo cierra
    #Con esta sintaxis se va a cerrar de manera automatica el archivo
    #se lo conoce como context manager o administrador de recursos
#print(archivo.read())
    #No hace falta try, ni el finally
    #En este contexto de with lo que se ejecuta de manera automatica
    #Son los metodos: __enter__ ,es donde se abre el archivo.
    #Otro metodo es el que cierra el archivo: __exit__.

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())

