#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector, json
import sys
import os
from urllib.parse import parse_qs

parse = parse_qs(os.environ.get("QUERY_STRING"))

dato1 = parse["texto"][0]
dato2 = parse["numero"][0]

sys.stderr.write("Dentro del insertardatos.py\n") # Escribe error en error.log

# --- Consulta a la BDD ---

my_database = mysql.connector.connect( # Crear la coneion a la BDD
    host="localhost",
    user="pruebaAjax",
    password="admin",
    database="pruebaAjax"
)

my_cursor = my_database.cursor() # Crear el cursor para hacer la consulta

query = f"insert into datos(dato1, dato2) values('{dato1}',{dato2})" # Crear el texto de la consulta

my_cursor.execute(query) # Ejecutar la consulta


my_database.commit() # Obligatorio el commit

# Cerrar cursor y bdd
my_cursor.close()
my_database.close()


# --- Generar salida para el cliente AJAX ---

print("Content-type: application/json\n")

print(json.dumps("ok"))

sys.stderr.write("Fin de pedirdatos.py") # Escribe error en error.log