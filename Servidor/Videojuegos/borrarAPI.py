#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideoJuegos
import json
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
    print(json.dumps(True))
else:
    print(json.dumps(False))


bd.cerrarBD()
