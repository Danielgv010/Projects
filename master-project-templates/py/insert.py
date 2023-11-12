#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

# Este python permite insertar un registro en la BDD con los datos introducidos en el formulario

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

data_directory = '../data/';data_file = 'accounts.json' # Ruta del archivo .json

def parameter_validation(): # Comprueba que se envían todos los parametros y devuelve dichos parámetros
    expected_parameters = ["name","company","theme","player-count","release-date"]

    for expected in expected_parameters: # Por cada parámetro esperado, comprueba que no falte o que no esté vacío
        if expected not in parameter: # Si falta en la url
            htmlCode.message_page("error",f"{expected} parameter cant be missing", "main.py")
            exit()
        if parameter[expected][0] == "": # Si el parámetro está vacío
            htmlCode.message_page("error",f"{expected} cant be empty", "main.py")
            exit()

    #Recupera los parámetros de la URL
    name = parameter["name"][0]
    company = parameter["company"][0]
    theme = parameter["theme"][0]
    player_count = parameter["player-count"][0]
    release_date = parameter["release-date"][0]

    return name,company,theme,player_count,release_date

column_name = ["name","company","theme","player_count","release_date"] # Nombres de las columnas de la BDD

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

database.insert("videojuegosantiguos",column_name,parameter_validation()) # Inserta los parámetros en la BDD

database.close_database()

htmlCode.message_page("success", "Row inserted", "crud.py")
