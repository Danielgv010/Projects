#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml, json
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
parametro = parse_qs(parametros[4])

producto = [parametro["producto"][0],parametro["cantidad"][0]]

#Abrimos el fichero para escribir
fichero = open("../datos/listaCompra.json")

if os.path.getsize("../datos/listaCompra.json") == 0: #Si el fichero no esta vacio
    lista_productos = [producto]
else:
    fichero = open("../datos/listaCompra.json")
    lista_productos = json.load(fichero)
    lista_productos.append(producto)

lista_json = json.dumps(lista_productos)
fichero = open("../datos/listaCompra.json","wt")
fichero.write(lista_json)
fichero.close()


#Creamos el inicio del HTML
codigoHtml.html_recarga()