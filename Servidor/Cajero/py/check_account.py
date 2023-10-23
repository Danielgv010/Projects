#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import atm_GUI
import os, json
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parameters = urlparse(ru)
parameter = parse_qs(parameters[4])

account_id = int(parameter["id"][0])

data_directory = "../data/"
data_file = "accounts.json"

table_row = ""

# Abre el fichero en modo lectura
file = open(data_directory+data_file)
# Se carga el fichero en la variable accounts
accounts = json.load(file)

# Se crea el principio de la página
atm_GUI.check_account_page_start()
for account in accounts: # Por cada cuenta
    if account_id == account[0]: # Si el id de la cuenta coincide con la cuenta seleccionada
        #Crea los elementos de la primera parte de la página con el id, numero de cuenta y saldo
        print(f"<h3>ID: {account[0]}</h3> <h1>Account Number: {account[1]}</h1> <h2>Balance: {account[2]}</h2>")
        #Crea los elementos entre la informacion de la cuenta y el historial de operaciones
        atm_GUI.check_account_page_middle()
        for operation in account[4]: # Por cada operacion de la cuenta
            if operation.startswith("+"): # Si la operacion empieza por +
                # Crea una fila verde con la información de la operación
                table_row = f"<tr class='green-tr'><td>{operation}</td></tr>{table_row}"
                # Como ya se ha encontrado la cuenta se rompe el bucle para ahorrar recursos
                break
            else: # Si la operacion no empieza por +
                # Crea una fila roja con la información de la operación
                table_row = f"<tr class='red-tr'><td>{operation}</td></tr>{table_row}"
                # Como ya se ha encontrado la cuenta se rompe el bucle para ahorrar recursos
                break
        # Imprime la fila
        print(table_row)
#Crea el final de la página
atm_GUI.check_account_page_end()