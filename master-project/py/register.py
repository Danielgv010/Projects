#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

print('Content-type: text/html\n')

import htmlCode
import os, json, hashlib
from urllib.parse import parse_qs

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

# Fichero con datos
data_directory = '../data/';data_file = 'accounts.json'

def parameter_validation(): # Valida que los parametros sean correctos
    if 'password' not in parameter: # Comprueba que no falte el parametro password
        #Muestra página de error
        htmlCode.message_page('error','Password missing','main.py')
        exit() # Se sale del python
    if 'email' not in parameter: # Comprueba que no falte el parametro email
        #Muestra página de error
        htmlCode.message_page('error','Email missing','main.py')
        exit() # Se sale del python

    # Separa los parametros en variables
    password = parameter['password'][0]
    email = parameter['email'][0]

    if password == '' or len(password)<4: # Comprueba que el parametro password no esté vacío y tenga 5 caracteres o mas
        #Muestra página de error
        htmlCode.message_page('error','Password error, 5 letters minimum','main.py')
        exit() # Se sale del python
    if email == '' or email.count('@')!=1: # Comprueba que el parametro email no esté vacío y contenga solo una @
        #Muestra página de error
        htmlCode.message_page('error','Email cant be empty and must containt just 1 @','main.py')
        exit() # Se sale del python

    password_encode = hashlib.sha512(str.encode(password)).hexdigest() # Encripta la contraseña para guardarla posteriormente

    return password_encode, email

def check_file(): # Comprueba que existe el fichero, si no existe lo crea y le añade []
    try:
        # Abre el fichero en modo escritura
        file = open(data_directory+data_file,'r') # La wt la quite porque el os.path.getsize de abajo devolvia 0, asi funciona
    except:
        # Abre el fichero en modo escritura
        file = open(data_directory+data_file,'x')

    if os.path.getsize(data_directory+data_file) == 0: # Si el fichero está vacío
        file.close()
        file = open(data_directory+data_file,'wt')
        file.write('[]')

    # Cierra el fichero
    file.close()

user = parameter_validation()  # Crea una lista con los parametros password e email

check_file()

with open(data_directory+data_file) as file: # Abre el fichero en modo lectura
    try:
        user_list = json.load(file) # Carga el .json como una lista
    except:
        user_list = [] # Crea una lista vacia

user_not_found = True # Usuario no repetido

for user_iterator in user_list: # Por cada usuario en la lista de usuarios
    if user_iterator[1]==user[1] : # Si coincide el email
        user_not_found = False # Usuario repetido
        break

if user_not_found: # Si el usuario no existe en la lista
    user_list.append(user) # Une el nuevo usuario con la lista

else: # Si el usuario existe en la lista
    #Muestra página de error
    htmlCode.message_page('error','User already exists'+'main.py')
    exit() # Se sale del python

with open(data_directory+data_file,'wt') as file: # Abre el fichero en modo escritura
    json.dump(user_list,file) # Guarda la lista en el .json

#Muestra página de éxito
htmlCode.message_page('success','Youve registered an account','main.py')