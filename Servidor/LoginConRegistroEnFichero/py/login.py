#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, json
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parameters = urlparse(ru)
parameter = parse_qs(parameters[4])

name = parameter["name"][0]
password = parameter["password"][0]

data_directory = "../data/"
data_file = "accounts.json"
file = None

if os.path.getsize(data_directory+data_file) != 0:
    correct = False
    
    file = open(data_directory+data_file)
    accounts = json.load(file)

    for account in accounts:
        if name == account[0] and password == account[2]:
            correct = True
            break

    if correct:
        print("login")
    else:
        print("bad password")