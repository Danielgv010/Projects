#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/plain\n")

import os
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

figura = int(param["figura"][0])
num_fila = int(param["nfilas"][0])

def cuadrado(filas): #Dibuja un cuadrado de asteriscos de x filas y x columnas
    for i in range(filas): #Bucle para crear las filas
        linea = "" #Vacía la línea con cada iteracion de filas
        for j in range(filas): #Bucle para crear las columnas
            linea+="*" #Rellena la línea
        print(linea) #Dibuja la línea

def triangulo(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas): #Bucle para crear las filas
        linea = "" #Vacía la línea con cada iteracion de filas
        for j in range(i+1): #Bucle para crear las columnas
            linea+="*" #Rellena la línea
        print(linea) #Dibuja la línea

def trianguloVuelta(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas,0,-1):
    #for i in range(filas): #Bucle para crear las filas
        linea = "" #Vacía la línea con cada iteracion de filas
        for j in range(i):
        #for j in range(filas-i): #Bucle para crear las columnas
            linea+="*" #Rellena la línea
        print(linea) #Dibuja la línea

def trianguloMirror(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas):
        linea = ""
        for j in range(filas - i - 1):
            linea+="-"
        for j in range(i+1):
            linea+="*"
        print(linea)

def trianguloVueltaMirror(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas):
        linea = ""
        for j in range(i):
            linea+="-"
        for j in range(filas-i):
            linea+="*"
        print(linea)

def cuadrado2(filas): #Dibuja un cuadrado de asteriscos de x filas y x columnas
    for i in range(filas): #Bucle para crear las filas
        linea = "" #Vacía la línea con cada iteracion de filas

def triangulo2(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas): #Bucle para crear las filas
        linea = "" #Vacía la línea con cada iteracion de filas
        for j in range(i+1): #Bucle para crear las columnas
            linea+="*" #Rellena la línea
        print(linea) #Dibuja la línea

def trianguloVuelta2(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas,0,-1):
    #for i in range(filas): #Bucle para crear las filas
        linea = "" #Vacía la línea con cada iteracion de filas
        for j in range(i):
        #for j in range(filas-i): #Bucle para crear las columnas
            linea+="*" #Rellena la línea
        print(linea) #Dibuja la línea

def trianguloMirror2(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas):
        linea = ""
        for j in range(filas - i - 1):
            linea+="-"
        for j in range(i+1):
            linea+="*"
        print(linea)

def trianguloVueltaMirror2(filas): #Dibuja un triangulo de asteriscos de x filas
    for i in range(filas):
        linea = ""
        for j in range(i):
            linea+="-"
        for j in range(filas-i):
            linea+="*"
        print(linea)

match figura: #Permite seleccionar el tipo de figura
    case 1:
        cuadrado(num_fila)
    case 2:
        triangulo(num_fila)
    case 3:
        trianguloVuelta(num_fila)
    case 4:
        trianguloMirror(num_fila)
    case 5:
        trianguloVueltaMirror(num_fila)
    case 6:
        cuadrado2(num_fila)
    case 7:
        triangulo2(num_fila)
    case 8:
        trianguloVuelta2(num_fila)
    case 9:
        trianguloMirror2(num_fila)
    case 10:
        trianguloVueltaMirror2(num_fila)
    case _:
        print("Opcion no contemplada")