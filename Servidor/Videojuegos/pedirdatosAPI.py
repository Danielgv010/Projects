#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from BDvideojuegos import BDVideoJuegos
import json

# --- Generar salida para el cliente AJAX ---

print("Content-type: application/json\n")

bd = BDVideoJuegos()

result = bd.todosLosVideojuegos()

print(json.dumps(result))

bd.cerrarBD()