#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import htmlPages
import os, json
from urllib.parse import urlparse, parse_qs

# Obtener los parametros que envía el formulario
ru = os.environ.get("REQUEST_URI")
parameters = urlparse(ru)
parameter = parse_qs(parameters[4])

if "name" in parameter and "email" in parameter and "password" in parameter: # Si no faltan parametros en la url
    name = parameter["name"][0]
    email = parameter["email"][0]
    password = parameter["password"][0]
    # Estructura de los datos en una cuenta
    account = [name,email,password]

    # Direccion donde se guardan las cuentas
    data_directory = "../data/"
    data_file = "accounts.json"

    error = False


    if name != "" and email != "" and password != "": # Comprueba que se pasen datos en el formulario
        # Abre/Crea el fichero
        try:
            file = open(data_directory+data_file)
        except:
            file = open(data_directory+data_file,"x")


        if os.path.getsize(data_directory+data_file) == 0: # Si el fichero está vacío
            # Crea una cuenta directamente
            accounts = [account]
        else: # Si no está vacío
            #Cargamos las cuentas del fichero en la lista accounts
            accounts = json.load(file)
            for account_iterator in accounts: # Por cada cuenta que hay creada en el json
                if account_iterator[0] == name or account_iterator[1] == email: # Si coincide el nombre o el email de la nueva cuenta
                    error=True
                    break
            if not error: # Si no hay coincidencias en el nombre o email
                # Añade la cuenta nueva a la lista
                accounts.append(account)


        if not error: # Si no hay coincidencias en el nombre o email
            # Convierte la lista de cuentas en un formato json
            accounts_parse_json = json.dumps(accounts)
            #Abre el fichero en modo sobreescritura
            file = open(data_directory+data_file,"wt")
            #Sobreescribe el json con el nuevo json
            file.write(accounts_parse_json)
            htmlPages.info_page("success","You've created a new account","index.html")

        #Cierra el fichero
        file.close()

    else: # Si hay parametros en blanco
        htmlPages.info_page("error","Fields must be completed","index.html")
else: # si faltan parametros
    htmlPages.info_page("error","Fields must be completed","index.html")