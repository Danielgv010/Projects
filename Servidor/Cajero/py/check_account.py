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

file = open(data_directory+data_file)
accounts = json.load(file)

for account in accounts:
    if account_id == account[0]:
        print(f"{account[0]}<br> {account[1]}<br> {account[2]}<br> {account[4]}")