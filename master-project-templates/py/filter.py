#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

# Este python permite mostrar la tabla html con los registros filtrados con los datos introducidos en el formulario

from urllib.parse import parse_qs
import os
import htmlCode
import modules.database

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))
values = []

def parameter_validation(): # Crea el filtro de la consulta SQL y devuelve la consulta
    query = ""
    missing = 0
    if "company" in parameter and parameter["company"][0]!="": # Si el parametro company está presente, lo añade a la consulta
        query += " company=%s"
        values.append(parameter["company"][0])
    else: # Si no está aumenta el contador de parámetros no enviado
        missing += 1
    if "theme" in parameter and parameter["theme"][0]!="": # Si el parametro theme está presente, lo añade a la consulta
        if query != "": # Si no es el primer parámetro en añadirse añade AND a la consulta
            query += " AND" 
        query += " theme=%s"
        values.append(parameter["theme"][0])
    else: # Si no está aumenta el contador de parámetros no enviado
        missing += 1
    if "player-count" in parameter and parameter["player-count"][0]!="": # Si el parametro player-count está presente, lo añade a la consulta
        if query != "": # Si no es el primer parámetro en añadirse añade AND a la consulta
            query += " AND"
        query += " player_count=%s"
        values.append(parameter["player-count"][0]) 
    else: # Si no está aumenta el contador de parámetros no enviado
        missing += 1
    if "from-year" in parameter and parameter["from-year"][0]!="": # Si el parametro from-year está presente, lo añade a la consulta
        if query != "": # Si no es el primer parámetro en añadirse añade AND a la consulta
            query += " AND"
        query += " release_date>=%s"
        values.append(parameter["from-year"][0]) 
    else: # Si no está aumenta el contador de parámetros no enviado
        missing += 1
    if "until" in parameter and parameter["until"][0]!="": # Si el parametro until está presente, lo añade a la consulta
        if query != "": # Si no es el primer parámetro en añadirse añade AND a la consulta
            query += " AND"
        query += " release_date<=%s" # Se añade company a la consulta
        values.append(parameter["until"][0]) 
    else: # Si no está aumenta el contador de parámetros no enviado
        missing += 1

    if missing == 5: # Si no se han envíado ninguno de los valores del filtro muestra la tabla sin filtros
        htmlCode.message_page("success","Filter applied","crud.py")
        exit()
    return query

database = modules.database.Database_Manager("localhost","videojuegos","videojuegos","videojuegos") # Hace una conexion con la base de datos

htmlCode.crud(database.custom_query_fetch("videojuegosantiguos",parameter_validation(), values)) # Crea la tabla con los datos que devuelve custom_query_fetch

database = database.close_database()
