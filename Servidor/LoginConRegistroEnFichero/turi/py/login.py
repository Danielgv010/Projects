#!C:\Users\deras\AppData\Local\Programs\Python\Python310\python.exe


import htmlPages
import http.cookies, uuid
import os, json, hashlib
from urllib.parse import parse_qs

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get("QUERY_STRING"))

# Fichero con datos
data_directory = "../data/";data_file = "accounts.json"

if "name" not in parameter: # Comprueba que no falte el parametro name
    #Muestra página de error
    htmlPages.info_page("error","Name is missing","../index.html")
    exit() # Se sale del python

if "password" not in parameter: # Comprueba que no falte el parametro password
    #Muestra página de error
    htmlPages.info_page("error","Password is missing","../index.html")
    exit() # Se sale del python

name = parameter["name"][0]
password = parameter["password"][0]

password_encode = hashlib.sha512(str.encode(password)).hexdigest() # Encripta la contraseña en sha512

with open(data_directory+data_file) as file: # Abre el fichero en modo lectura
    try:
        user_list = json.load(file) # Carga el .json como una lista
    except:
        user_list = [] # Crea una lista vacia

user_found = False
for user_iterator in user_list: # Por cada usuario en la lista de usuarios
    if user_iterator[0]==name and user_iterator[1]==password_encode: # Si coincide el nombre y la contraseña
        user_found = True
        break

if not user_found: # Si no coincide el usuario y la contraseña
    #Muestra página de error
    htmlPages.info_page("error","Bad login","../index.html")
    exit() # Se sale del python

# Crear la cookie para el control de sesion
print("Content-Type: text/html")
cookie = http.cookies.SimpleCookie() # Crea la estructura de la cookie
cookie["LOGIN"] = uuid.uuid4() # Crea una cookie con un identificador aleatorio como valor

print(cookie) # Imprime la cookie
print()

# Muesta la página de éxito
htmlPages.info_page("success",f"You logged in as {user_iterator[0]}","page1.py")