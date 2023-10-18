#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/plain\n")

import os

directorio = "datos/"
nombre_fichero = "palabras.dat"

'''
#Los \n los cuenta al leer el fichero

try:
    #Abre el fichero especificado para leer
    #fichero = open(directorio+nombre_fichero)
    # Lo mismo  =  open(directorio+nombre_fichero, "rt")

    #Abre el fichero para añadir texto
    #fichero = open(directorio+nombre_fichero,"at")

    #Abre el fichero para sobreescribir
    #fichero = open(directorio+nombre_fichero,"w")

    #Crea el fichero si no existe y permite escribir
    fichero = open(directorio+nombre_fichero,"x")



except:
    print("problema al abrir el fichero")

else:
    #Añade al final de la línea, no crea una nueva
    #Para eso el \n
    fichero.write("y vuelta a empezar")


    #Guarda todas las lineas del fichero como valores de un array
    #Quita los saltos de línea con el .strip por cada línea
    #lista_dias = [dia.strip("\n") for dia in fichero.readlines()]
    #if "Lunes" in lista_dias:
    #    print("Está el lunes")
    #for dias in lista_dias:
    #    print(dias)


    #Lee una linea del fichero y la guarda en una variable
    #contenido = fichero.readline()

    #Imprime la línea leída y la longitud en caracteres
    #print(contenido)
    #print(len(contenido))

    #Lee el fichero al completo (Si se ha hecho un readline antes, continúa desde esa línea)
    #y lo guarda en una variable
    #contenido = fichero.read()
    #Lo mismo que:
    #for contenido in fichero:
    #    print(contenido)
    #o
    #while contenido:
    #   print(contenido)
    #   contenido = fich.readline
    ##### Con un break se rompe el while y también el else
    #else:
    #   print("Fin de fichero")

    #Imprime las líneas del fichero y la longitud en caracteres
    #print(contenido)
    #print(len(contenido))

finally:
    #Cierra el fichero
    fichero.close()
'''


#Para saber el directorio actual de trabajo
print(os.getcwd())

#Devuevle true si le pasamos un directorio
print(os.path.isdir(directorio))

#Devuelve true si le pasamos un fichero
print(os.path.isfile(directorio+nombre_fichero))

#Nos permite cambiar de directorio
os.chdir(directorio)
print(os.getcwd())

fichero = open(nombre_fichero)
print(fichero.readlines())
fichero.close()
