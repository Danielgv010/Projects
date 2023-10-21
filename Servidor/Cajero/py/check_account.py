#!C:\Users\deras\AppData\Local\Programs\Python\Python310\python.exe

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

file = open(data_directory+data_file)
accounts = json.load(file)

atm_GUI.check_account_page_start()
for account in accounts:
    if account_id == account[0]:
        print(f"<h3>ID: {account[0]}</h3> <h1>Account Number: {account[1]}</h1> <h2>Balance: {account[2]}</h2>")
        atm_GUI.check_account_page_middle()
        for operation in account[4]:
            if operation.startswith("+"):
                table_row = f"<tr class='green-tr'><td>{operation}</td></tr>{table_row}"
            else:
                table_row = f"<tr class='red-tr'><td>{operation}</td></tr>{table_row}"
        print(table_row)
atm_GUI.check_account_page_end()