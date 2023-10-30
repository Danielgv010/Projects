#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html")

import http.cookies
import htmlPages
import os, json
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parameters = urlparse(ru)
parameter = parse_qs(parameters[4])

cookie = http.cookies.SimpleCookie()

if "name" in parameter and "password" in parameter: # Si no faltan parametros en la url
    name = parameter["name"][0]
    password = parameter["password"][0]

    data_directory = "../data/"
    data_file = "accounts.json"


    if name != "" and password != "": # Si los parametros no vienen en blanco
        if os.path.getsize(data_directory+data_file) != 0: # Si el fichero no està vacío
            correct = False
            
            # Abre el fichero
            file = open(data_directory+data_file)
            # Carga el json en la lista accounts
            accounts = json.load(file)

            for account_iterator in accounts: # Por cada cuenta en la lista cuentas
                if name == account_iterator[0] and password == account_iterator[2]: # Si coincide el nombre y la contraseña
                    correct = True
                    break

            if correct: # Si coincide el nombre y la contraseña
                cookie["Login"] = True
                print(cookie)
                htmlPages.info_page("success","You've logged in","pagina1.py")
            else: # Si no coinciden
                htmlPages.info_page("error","Your user name or password are incorrect","index.html")