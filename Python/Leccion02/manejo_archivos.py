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