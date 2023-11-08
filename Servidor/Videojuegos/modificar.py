#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos
import os
from urllib.parse import urlparse, parse_qs

print("Content-type: text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

bd = BDVideoJuegos()

if "nombre" in param and param["nombre"][0] != "" \
        and "empresa" in param and param["empresa"][0] != "" \
        and "tematica" in param and param["tematica"][0] != "" \
        and "nJug" in param and param["nJug"][0] != "" \
        and "anio" in param and param["anio"][0] != "" \
        and "id" in param and param["id"][0] != "":

    # Capturar los datos a insertar
    nombre = param["nombre"][0]
    empresa = param["empresa"][0]
    tematica = param["tematica"][0]
    nJug = param["nJug"][0]
    anio = param["anio"][0]
    id = param["id"][0]

    # Insertar en la base de datos
    bd.modificar(id, nombre, empresa, tematica, nJug, anio)
    HtmlVideoJuegos.error("Dato Modificado")
else:
    HtmlVideoJuegos.error("Algún parámetro no es correcto")


# Cerrar base de datos
bd.cerrarBD()
