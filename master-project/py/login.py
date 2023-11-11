#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import htmlCode
import os, json, hashlib
from urllib.parse import parse_qs
import http.cookies, uuid

# Fichero con datos
data_directory = '../data/';data_file = 'accounts.json'

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

if 'password' not in parameter: # Si no está password en los parametros
    # Muestra página de error
    htmlCode.message_page('error','Login error','index.html') 
    exit() # Se sale del python
if 'email' not in parameter: # Si no está email en los parametros
    # Muestra página de error
    htmlCode.message_page('error','Login error','index.html') 
    exit() # Se sale del python

password = parameter['password'][0]
email = parameter['email'][0]

password_encode = hashlib.sha512(str.encode(password)).hexdigest() # Encripta la contraseña en sha512

with open(data_directory+data_file) as file:
    try:
        account_list = json.load(file)
    except:
        account_list = []

    for account_iterator in account_list:
        if account_iterator[0] == password_encode and account_iterator[1]==email:
            # Crear la cookie para el control de sesion
            print('Content-Type: text/html')
            cookie = http.cookies.SimpleCookie() # Crea la estructura de la cookie
            cookie['LOGIN'] = uuid.uuid4() # Crea una cookie con un identificador aleatorio como valor

            print(cookie) # Imprime la cookie
            print()

            # Muesta la página de éxito
            htmlCode.message_page('success','Youve logged in','crud.py')
            exit()
        else:
            htmlCode.message_page('error','Bad login','index.html')
            exit()
