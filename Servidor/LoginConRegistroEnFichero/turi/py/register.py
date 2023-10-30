#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import htmlPages
import os, json, hashlib
from urllib.parse import parse_qs

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get("QUERY_STRING"))

# Fichero con datos
data_directory = "../data/";data_file = "accounts.json"

def parameter_validation(): # Valida que los parametros sean correctos
    if "name" not in parameter: # Comprueba que no falte el parametro name
        #Muestra página de error
        htmlPages.info_page("error","Name missing","../index.html")
        exit() # Se sale del python
    if "password" not in parameter: # Comprueba que no falte el parametro password
        #Muestra página de error
        htmlPages.info_page("error","Password missing","../index.html")
        exit() # Se sale del python
    if "email" not in parameter: # Comprueba que no falte el parametro email
        #Muestra página de error
        htmlPages.info_page("error","Email missing","../index.html")
        exit() # Se sale del python

    # Separa los parametros en variables
    name = parameter["name"][0]
    password = parameter["password"][0]
    email = parameter["email"][0]

    if name == "": # Comprueba que el parametro name no esté vacío
        #Muestra página de error
        htmlPages.info_page("error","Name cant be empty","../index.html")
        exit() # Se sale del python
    if password == "" or len(password)<4: # Comprueba que el parametro password no esté vacío y tenga 5 caracteres o mas
        #Muestra página de error
        htmlPages.info_page("error","Password error, 5 letters minimum","../index.html")
        exit() # Se sale del python
    if email == "" or email.count("@")!=1: # Comprueba que el parametro email no esté vacío y contenga solo una @
        #Muestra página de error
        htmlPages.info_page("error","Email cant be empty and must containt just 1 @","../index.html")
        exit() # Se sale del python

    password_encode = hashlib.sha512(str.encode(password)).hexdigest()

    return name, password_encode, email

def check_file(): # Comprueba que existe el fichero, si no existe lo crea y le añade []
    try:
        # Abre el fichero en modo escritura
        file = open(data_directory+data_file,"wt")
    except:
        # Abre el fichero en modo escritura
        file = open(data_directory+data_file,"x")

    if os.path.getsize(data_directory+data_file) == 0: # Si el fichero está vacío
        file.write("[]")
        pass

    # Cierra el fichero
    file.close()

user = parameter_validation()  # Crea una lista con los parametros name, password e email

check_file()

with open(data_directory+data_file) as file: # Abre el fichero en modo lectura
    try:
        user_list = json.load(file) # Carga el .json como una lista
    except:
        user_list = [] # Crea una lista vacia

user_not_found = True # Usuario no repetido

for user_iterator in user_list: # Por cada usuario en la lista de usuarios
    if user_iterator[0]==user[0] or user_iterator[2]==user[2]: # Si coincide el nombre o el email
        user_not_found = False # Usuario repetido
        break

if user_not_found: # Si el usuario no existe en la lista
    user_list.append(user) # Une el nuevo usuario con la lista
else: # Si el usuario existe en la lista
    htmlPages.info_page("error","User already exists"+"../index.html")
    exit()

with open(data_directory+data_file,"wt") as file: # Abre el fichero en modo escritura
    json.dump(user_list,file) # Guarda la lista en el .json

#Muestra página de éxito
htmlPages.info_page("success","You've registered an account","../index.html")