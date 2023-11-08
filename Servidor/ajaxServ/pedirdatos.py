#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import mysql.connector
import sys,json

sys.stderr.write("Dentro del pedirdatos.py\n") # Escribe error en error.log

# --- Consulta a la BDD ---

my_database = mysql.connector.connect( # Crear la coneion a la BDD
    host="localhost",
    user="pruebaAjax",
    password="admin",
    database="pruebaAjax"
)

my_cursor = my_database.cursor() # Crear el cursor para hacer la consulta

query = "SELECT * FROM datos" # Crear el texto de la consulta

my_cursor.execute(query) # Ejecutar la consulta

result = my_cursor.fetchall() # Obtener las filas de la consulta y guardar en la variable

sys.stderr.write(str(result)) # Traza para ver el objeto resultado

# Cerrar cursor y bdd
my_cursor.close()
my_database.close()


# --- Generar salida para el cliente AJAX ---

print("Content-type: application/json\n")

print(json.dumps(result))

sys.stderr.write("Fin de pedirdatos.py") # Escribe error en error.log