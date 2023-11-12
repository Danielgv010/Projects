#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import htmlCode
import os, json, hashlib
from urllib.parse import parse_qs

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

data_directory = '../data/';data_file = 'accounts.json' # Ruta del archivo .json


def parameter_validation(): # Comprueba que se hayan pasado los parámetros y los devuelve con la contraseña encriptada
    expected_parameters = ["name","email","password"]

    for expected in expected_parameters: # Por cada parámetro esperado, comprueba que no falte o que no esté vacío
        if expected not in parameter: # Si falta en la url
            htmlCode.message_page("error",f"{expected} parameter cant be missing", "main.py")
            exit()
        if parameter[expected][0] == "": # Si el parámetro está vacío
            htmlCode.message_page("error",f"{expected} cant be empty", "main.py")
            exit()

    #Recupera los parámetros de la URL
    name = parameter["name"][0]
    email = parameter["email"][0]
    password = parameter["password"][0]

    if len(password)<=4: # Si la contraseña tiene menos de 5 caracteres
        htmlCode.message_page("error","Password must have more than 4 characters", "main.py")
        exit()

    if "@" not in email: # Si el email no tiene una @
        htmlCode.message_page("error","Email must have @", "main.py")
        exit()

    
    password_encode = hashlib.sha512(str.encode(password)).hexdigest() # Encripta la contraseña

    return name,email,password_encode

def check_file(): # Comprueba que exista el fichero y que no esté vacío
    try: # Prueba a abrir el fichero en modo lectura
        file = open(data_directory+data_file,"r")
    except: # Si no puede lo crea
        file = open(data_directory+data_file,"x")

    if os.path.getsize(data_directory+data_file) == 0: # Si el fichero está vacío
        file.close()
        file = open(data_directory+data_file,'wt') # Abre el fichero en modo sobreescritura
        file.write("[]") # Escribe [] en el fichero
    file.close()

account = parameter_validation() # Guarda los datos de la cuenta en una variable
check_file() # Comprueba la existencia del fichero y que no esté vacío

with open(data_directory+data_file,"r") as file: # Abre el fichero en modo lectura
    try: # Prueba a cargar el fichero json
        account_list = json.load(file)
    except: # Si está vacío crea una lista vacía
        account_list = []

for account_iterator in account_list: # Por cada cuenta en la lista de cuentas
    if account_iterator[1]==account[1]: # Si el email ya está registrado
        htmlCode.message_page("error","Repeated account", "main.py")
        exit()

account_list.append(account) # Añade la nueva cuenta a la lista de cuentas

with open(data_directory+data_file,"wt") as file: # Abre el fichero en modo sobreescritura
    json.dump(account_list,file) # Guarda la lista de cuentas en formato json en el fichero

htmlCode.message_page("success","Youve registered an account", "main.py")
