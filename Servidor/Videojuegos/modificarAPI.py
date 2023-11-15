#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import os,json
from urllib.parse import urlparse, parse_qs


from BDvideojuegos import BDVideoJuegos


print("Content-type: application/json\n")


ru = os.environ.get("REQUEST_URI")
parametros = urlparse(ru)
param = parse_qs(parametros[4])


#acceder a la base de datos
bd = BDVideoJuegos()


if "id" in param and param["id"][0]!="":
    #capturar los datos a insertar
    id = param["id"][0]


    #borrar de la base de datos
    print(json.dumps(bd.seleccionaPorId(id)))




#cerrar base de datos
bd.cerrarBD()
