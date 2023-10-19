#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
parametro = parse_qs(parametros[4])

producto = parametro["producto"][0]
cantidad = parametro["cantidad"][0]

#Abrimos el fichero para escribir
fichero = open("../datos/listaCompra.dat", "at")

if os.path.getsize("../datos/listaCompra.dat") != 0: #Si el fichero no esta vacio
    fichero.write("\n")

#Se añade el producto y la cantidad separados por ;
fichero.write(f"{producto};{cantidad}")

#Cerramos el fichero
fichero.close()

#Creamos el inicio del HTML
codigoHtml.html_recarga()