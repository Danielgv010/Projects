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
quantity = float(parameter["quantity"][0])
operation = parameter["operation"][0]

file = open(data_directory+data_file)
accounts = json.load(file)

def deposit():
    global operation_error
    for account in accounts:
        if account[0] == account_id:
            operation_error = 0
            account[2] += quantity
            account[4].append(f"+{quantity}")

def withdraw():
    global operation_error
    for account in accounts:
        if account[0] == account_id and account[2]>=quantity:
            account[2] -= quantity
            account[4].append(f"- {quantity}")
            operation_error = 0 
            break
        else:
            operation_error = 1

if operation == "deposit":
    deposit()
elif operation == "withdraw":
    withdraw()

if operation_error == 1:
    atm_GUI.operation_not_done()
else:
    file = open(data_directory+data_file,"wt")
    accounts_parse_json = json.dumps(accounts)
    file.write(accounts_parse_json)
    file.close()
    atm_GUI.operation_done()