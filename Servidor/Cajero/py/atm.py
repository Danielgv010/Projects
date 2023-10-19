#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import atm_GUI
import os, json

data_directory = "../data/"
data_file = "accounts.json"
file = None
account = []

atm_GUI.pagina_principal()

def read_file():
    json_file = json.load(data_directory+data_file)
    print(json_file)

if len(os.listdir(data_directory)) != 0:
    file = open(data_directory+data_file)
else:
    file = open(data_directory+data_file,"x")


read_file()
file.close()