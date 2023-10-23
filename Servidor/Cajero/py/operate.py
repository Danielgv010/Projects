#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import atm_GUI
import os, json
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parameters = urlparse(ru)
parameter = parse_qs(parameters[4])

data_directory = "../data/"
data_file = "accounts.json"

account_id = int(parameter["account"][0])
ammount = int(parameter["ammount"][0])
operation = parameter["operation"][0]

if account_id != 0: # Si al operar se ha seleccionado alguna cuenta
    # Se abre el fichero en modo lectura
    file = open(data_directory+data_file)
    # Se carga el fichero en la variable accounts
    accounts = json.load(file)

    def deposit(): # Hace el deposito de dinero en la cuenta
        global operation_error
        for account in accounts: # Por cada cuenta
            if account[0] == account_id: # Si hay alguna cuenta que sea del id proporcionado en el select
                # No hay error
                operation_error = 0
                # Se suma el saldo al que había en la cuenta
                account[2] += ammount
                # Se añade la operación al historial de operaciones de la cuenta
                account[4].append(f"+{ammount}")
                # Como ya se ha encontrado la cuenta se rompe el bucle para ahorrar recursos
                break

    def withdraw(): # Hace la retirada de dinero de la cuenta
        global operation_error
        for account in accounts: # Por cada cuenta
            if account[0] == account_id and account[2]>=ammount: # Si hay alguna cuenta que sea del id proporcionado en el select y tiene más o el mismo saldo del que se quiere retirar
                # No hay error
                operation_error = 0 
                # Se resta el saldo del que había en la cuenta
                account[2] -= ammount
                # Se añade la operación al historial de operaciones de la cuenta
                account[4].append(f"- {ammount}")
                # Como ya se ha encontrado la cuenta se rompe el bucle para ahorrar recursos
                break
            else: # Si no hay ninguna cuenta que sea del id proporcionado en el select o tiene menos saldo del que se quiere retirar
                # Hay error
                operation_error = 1

    # Compara que operación se ha seleccionado y actua en consecuencia
    if ammount > 0: # Si el ammount no es 0 o inferior
        operation_error = 0
        if operation == "deposit":
            deposit()
        elif operation == "withdraw":
            withdraw()
    else:
        operation_error = 1

    if operation_error == 1: # Si hay error
        # Muestra una página que indica que la operación no se ha completado
        atm_GUI.operation_not_done()
    else: # Si no hay error
        # Se abre el fichero en modo sobreescritura
        file = open(data_directory+data_file,"wt")
        # Se convierte la variable accounts en formato json
        accounts_parse_json = json.dumps(accounts)
        # Se sobreescribe el fichero con lo incluido en la variable accounts_parse_json
        file.write(accounts_parse_json)
        # Se cierra el fichero
        file.close()
        # Se muestra una página donde se indica que la operación se ha completado
        atm_GUI.operation_done()
else: # Si no se ha seleccionado una cuenta existente
    # Muestra una página que indica que la operación no se ha completado
    atm_GUI.operation_not_done()