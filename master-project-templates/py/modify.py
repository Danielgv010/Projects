#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

# Este python permite modificar el registro sobre el que el usuario haya hecho clic en modificar

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

def parameter_validation():  # Comprueba que se hayan pasado los parámetros y los devuelve
    expected_parameters = ["id","name","company","theme","player-count","release-date"]

    for expected in expected_parameters: # Por cada parámetro esperado, comprueba que no falte o que no esté vacío
        if expected not in parameter: # Si falta en la url
            htmlCode.message_page("error",f"{expected} parameter cant be missing", "main.py")
            exit()
        if parameter[expected][0] == "": # Si el parámetro está vacío
            htmlCode.message_page("error",f"{expected} cant be empty", "main.py")
            exit()

    #Recupera los parámetros de la URL
    id = parameter["id"][0]
    name = parameter["name"][0]
    company = parameter["company"][0]
    theme = parameter["theme"][0]
    player_count = parameter["player-count"][0]
    release_date = parameter["release-date"][0]

    return id,name,company,theme,player_count,release_date

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

column_name = ["name","company","theme","player_count","release_date"]
validated_parameters = parameter_validation() # Recupera los parametros de la URL a través del metodo parameter_validation
column_values = validated_parameters[1:] # Guarda todo el array excepto la primera posicion (ID)

database.modify("videojuegosantiguos",column_name,column_values,["id"],validated_parameters[:1]) # Modifica el registro que coincide el id con la primera posicion del array column_values

database.close_database()

htmlCode.message_page("success", "Row modified", "crud.py")
