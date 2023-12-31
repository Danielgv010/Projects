#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos
import os
from urllib.parse import urlparse, parse_qs

print("Content-type: text/html\n")

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

bd = BDVideoJuegos()

if "id" in param and param["id"][0] != "":
    id = param["id"][0]
    bd.borrarPorId(id)

HtmlVideoJuegos.salidaPrincipal(bd.todosLosVideojuegos())

bd.cerrarBD()
