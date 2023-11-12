#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

# Este python muestra una página con un formulario el cual tiene los inputs rellenados con los datos del registro a modificar para que el usuario los edite

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

htmlCode.modify_window_crud(database.fetch_filtered("videojuegosantiguos","name",["id"],parameter["id"],1)) # Crea una pagina la cual tiene los inputs del registro rellenados con los datos del mismo

database.close_database()
