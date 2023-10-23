#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import atm_GUI
import json, os
import random

data_directory = "../data/"
data_file = "accounts.json"
# accounts = ["id","accounts_number", "balance", "inspect_button", ["operation_list"]]

def random_number(digits): # Crea un número aleatorio de x dígitos y lo devuelve
    number_string = ""
    for i in range(digits):
        #Genera y concatena los digitos
        number_string += str(random.randint(0,9))
    return number_string

def accounts_number_random(): # Crea el número de cuenta llamando a la función random_number y lo devuelve
    return f"ES{random_number(2)} {random_number(4)} {random_number(4)} {random_number(2)} {random_number(9)}"

def get_id(): # Genera los id de cuenta (Como no hay botón de borrar cuenta no hay problema de duplicados)
    counter = 1
    if os.path.getsize(data_directory+data_file) != 0: #Si el fichero no está vacio
        #Abre el fichero en modo lectura
        file = open(data_directory+data_file)
        #Carga el fichero en una variable
        accounts_temp = json.load(file)
        #Por cada cuenta creada suma 1 al contador y lo devuelve cuando no haya más cuentas
        # No hay cuentas --> return 1
        # Hay 1 cuenta --> return 1+1
        # ...
        for account in accounts_temp:
            counter += 1
    return counter

def create_account(): #Crea una cuenta con las funciones previamente creadas. El saldo empieza en 0 y el botón se crea apoyandose de la función get_id
    return [get_id(), accounts_number_random(), 0, f"<a href='check_account.py?id={get_id()}'><button>Check Account</button></a>", []]

if os.path.getsize(data_directory+data_file) == 0: # Si el fichero está vacío
    # Se guarda la nueva cuenta en una variable
    accounts = [create_account()]
else: # Si no está vacío
    # Se abre el fichero en modo lectura
    file = open(data_directory+data_file)
    # Se carga el fichero en la variable accounts
    accounts = json.load(file)
    # Se une la nueva cuenta a las guardadas en la variable accounts
    accounts.append(create_account())

# Se convierte la variable accounts en formato json
accounts_parse_json = json.dumps(accounts)
# Se abre el fichero en modo sobreescritura
file = open(data_directory+data_file,"wt")
# Se sobreescribe el fichero con lo incluido en la variable accounts_parse_json
file.write(accounts_parse_json)
# Se cierra el fichero
file.close()
# Se muestra una página donde se indica que la operación se ha completado
atm_GUI.operation_done()