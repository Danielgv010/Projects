#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideoJuegos
import json
import FormVideojuegos

print("Content-type: text/html\n")

bd = BDVideoJuegos()

miresultado = bd.juegosConFiltro(FormVideojuegos.crearFiltros())

print(json.dumps(miresultado))

bd.cerrarBD()
