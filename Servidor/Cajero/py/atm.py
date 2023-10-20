#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import atm_GUI
import os, json

data_directory = "../data/"
data_file = "accounts.json"
file = None
accounts = []

atm_GUI.home_page_start()

def list_accounts():
    if len(accounts) != 0:
        for account in accounts:
            print(f"<tr><td>{account[0]}</td><td>{account[1]}</td><td>{account[2]}</td><td>{account[3]}</td></tr>")
    else:
        print("<tr><td colspan='4'>There is no accounts</td></tr>")

def create_options():
    if len(accounts) != 0:
        for account in accounts:
            print(f"<option value='{account[0]}'>Account {account[0]}</option>")
    else:
        print("<option value='0'>You must create an account first</option>")

try:
    file = open(data_directory+data_file)
except:
    file = open(data_directory+data_file,"x")

if os.path.getsize(data_directory+data_file) != 0:
    accounts = json.load(file)
else:
    accounts = []

list_accounts()
file.close()

atm_GUI.home_page_middle()
create_options()
atm_GUI.home_page_end()