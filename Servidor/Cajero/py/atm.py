#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import atm_GUI
import os, json

data_directory = "../data/"
data_file = "accounts.json"
file = None

#Crea el inicio de la página hasta la tabla
atm_GUI.home_page_start()

def list_accounts(): #Mete toda la información asociada a las cuentas en una tabla
    if len(accounts) != 0: #Si hay cuentas
        for account in accounts:
            print(f"<tr><td>{account[0]}</td><td>{account[1]}</td><td>{account[2]}</td><td>{account[3]}</td></tr>")
    else: #Si no hay cuentas
        print("<tr><td colspan='4'>There is no accounts</td></tr>")

def create_options(): #Crea los <option> del select sugún las cuentas que hayan
    if len(accounts) != 0: #Si hay cuentas
        for account in accounts:
            print(f"<option value='{account[0]}'>Account {account[0]}</option>")
    else: #Si no hay cuentas
        print("<option value='0'>You must create an account first</option>")

try: #Si hay un fichero lo abre en modo lectura
    file = open(data_directory+data_file)
except: #Si no hay fichero lo crea
    file = open(data_directory+data_file,"x")

if os.path.getsize(data_directory+data_file) != 0: #Si el fichero no está vacío lo carga como lista en accounts
    accounts = json.load(file)
else: #Si el fichero está vacío crea una lista vacía en accounts
    accounts = []

list_accounts()

#Cierra el fichero
file.close()

#Crea desde la tabla hasta el select
atm_GUI.home_page_middle()
#Crea el select
create_options()
#Crea el resto de la página
atm_GUI.home_page_end()