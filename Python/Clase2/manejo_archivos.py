# Tarea realizada por Andrea Llavel
#                             ............**** manejo_archivos.py..........*
# declaramos una variable  
try:                       #Crear un archivo a traves del metodo open
    archivo = open('prueba.txt', 'w', encoding='utf8')   # w significa escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('como por ejemplo: accion, ejecucion y produccion\n')
    archivo.write('Las letras son:\nr read leer, \na append anexa, \nw write escribe, \nx crea un archivo')
    archivo.write('\nt es para texto o text, \nb archivos binarios, \nw+ lee y escribe son iguales r+\n')
    archivo.write('Saludos a todos los alumnos de la Tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:       # siempre se ejecuta
    archivo.close()      # Con esto se debe cerrar el archivo
#archivo.write('Todo quedo perfecto')    /este es un error input action excetion
#                                  .......***** Leer_archivo-py.......*****
# para leer un archivo read es el mod por default
archivo = open('prueba.txt', 'r', encoding='utf8')  #las letras son : r(read),a(append),w(write),x(crea)
# print(archivo.read())
#vamos anexar mas informacion y crea el archivo que no existe con la letra "a"
#print(archivo.read(16))
#print(archivo.read(10))   #Continuamos conla linea anterior
#print(archivo.readline())  #Nos muestra solo la primer linea escrita
#print(archivo.readline())  #Nos muestra la segunda linea de archivos
#No es necesario especificar la ruta de nuestro archivo, pero en caso de que
#se necesita hay que especificarlo.Por ejemplo buscar la ruta para encontrar el archivo,ejemplo c:\\
#vamos a iterar el archivo, cada una de las lineas
#for linea in archivo:
#print(linea): iteramos todos los elementos del archivo
#print(archivo.readlines()[11])
#Anexamos informacion, copiamos a otro
archivo2 = open('copia.txt', 'w', encoding='utf8')
archivo2.write(archivo.read())
archivo.close()    #Cerramos el primer archivo
archivo2.close()   #Cerramos el segundo archivo

print('Se ha terminado el proceso de leer y copiar archivos')
#Las veces que nosostros copiemos , se anexa a lo que ya estaba copiado
#Si ejecutamos "w" en lugar de "a" quitara el acceso de archivo que tenia
#                                  ..........***** ManejoArchivos.py******...........
class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')    #Encapsulamos el codigo dentro del metodo
        return self.nombre
    def __exit__(self, tipo_exception, valor_exception, traza_error):
        print('cerramos el recurso'.center(50, '-'))
        if self.nombre:
            self.nombre.close()   #Cerramos ahi el archivo
   #                                ........... ***archivos_con_with.py***..............
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
    #                                  ............. ***prueba.txt***...................
    Programamos con diferentes tipos de archivos, ahora txt.
Los acentos son importantes para las palabras
como por ejemplo: accion, ejecucion y produccion
Las letras son:
r read leer, 
a append anexa, 
w write escribe, 
x crea un archivo
t es para texto o text, 
b archivos binarios, 
w+ lee y escribe son iguales r+
Saludos a todos los alumnos de la Tecnicatura
Con esto terminamos
#                                        ...............***copia.txt***.................
Programamos con diferentes tipos de archivos, ahora txt.
Los acentos son importantes para las palabras
como por ejemplo: accion, ejecucion y produccion
Las letras son:
r read leer, 
a append anexa, 
w write escribe, 
x crea un archivo
t es para texto o text, 
b archivos binarios, 
w+ lee y escribe son iguales r+
Saludos a todos los alumnos de la Tecnicatura
Con esto terminamos
   

