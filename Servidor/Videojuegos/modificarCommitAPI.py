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


if "id" in param and param["id"][0]!="" \
    and "nombre" in param and param["nombre"][0]!="" \
    and "empresa" in param and param["empresa"][0]!="" \
    and "tematica" in param and param["tematica"][0]!="" \
    and "nJug" in param and param["nJug"][0]!="" \
    and "anio" in param and param["anio"][0]!="":
    #capturar los datos a insertar
    id = param["id"][0]
    nombre = param["nombre"][0]
    empresa = param["empresa"][0]
    tematica = param["tematica"][0]
    nJug = param["nJug"][0]
    anio = param["anio"][0]


    #borrar de la base de datos
    bd.modificar(id,nombre,empresa,tematica,nJug,anio)


    print(json.dumps(True))
else:
    print(json.dumps(False))


#cerrar base de datos
bd.cerrarBD()
