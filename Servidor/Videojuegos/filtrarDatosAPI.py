#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from BDvideojuegos import BDVideoJuegos
import json
import FormVideojuegos

print("Content-type: text/html\n")

bd = BDVideoJuegos()

miresultado = bd.juegosConFiltro(FormVideojuegos.crearFiltros())

print(json.dumps(miresultado))

bd.cerrarBD()
