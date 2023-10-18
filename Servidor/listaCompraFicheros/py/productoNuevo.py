#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, codigoHtml
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
parametro = parse_qs(parametros[4])

dato = parametro["producto"][0]

fichero = open("../datos/listaCompra.dat", "at")

fichero.write(f"\n {dato}")

fichero.close()

#Creamos el inicio del HTML
codigoHtml.inicio_cesta_compra()

print("Producto añadido")

codigoHtml.fin_cesta_compra()