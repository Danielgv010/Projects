#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

# Este python permite borrar el registro sobre el que se ha hecho clic en el boton de borrar

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

database.delete_with_id("videojuegosantiguos",parameter["id"]) # Borra un registro con el id que se le pasa a la funcion

database.close_database()

htmlCode.message_page("success", "Row deleted", "crud.py")
