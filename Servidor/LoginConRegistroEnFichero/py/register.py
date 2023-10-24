#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os, json
from urllib.parse import urlparse, parse_qs

ru = os.environ.get("REQUEST_URI")
parameters = urlparse(ru)
parameter = parse_qs(parameters[4])

name = parameter["name"][0]
email = parameter["email"][0]
password = parameter["password"][0]

account = [name,email,password]

data_directory = "../data/"
data_file = "accounts.json"
file = None

if name != "" and email != "" and password != "":
    try:
        file = open(data_directory+data_file)
    except:
        file = open(data_directory+data_file,"x")

    if os.path.getsize(data_directory+data_file) == 0:
        accounts = [account]
    else:
        accounts = json.load(file)
        accounts.append(account)

    accounts_parse_json = json.dumps(accounts)

    file = open(data_directory+data_file,"wt")
    file.write(accounts_parse_json)

    file.close()