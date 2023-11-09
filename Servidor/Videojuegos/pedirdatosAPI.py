#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideoJuegos
import json

# --- Generar salida para el cliente AJAX ---

print("Content-type: application/json\n")

bd = BDVideoJuegos()

result = bd.todosLosVideojuegos()

print(json.dumps(result))

bd.cerrarBD()