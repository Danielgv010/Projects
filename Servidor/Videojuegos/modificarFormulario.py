#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import os
from urllib.parse import urlparse, parse_qs
from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos

ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])

bd = BDVideoJuegos()

print("Content-type: text/html\n")

if "id" in param and param["id"][0]!="":
    id = param["id"][0]
    HtmlVideoJuegos.formularioModificar(bd.seleccionaPorId(id))
else:
    HtmlVideoJuegos.error("Falta el id")