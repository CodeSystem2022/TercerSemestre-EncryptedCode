# Andrea Llavel
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
