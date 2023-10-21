#!C:\Users\deras\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n")

import atm_GUI
import json, os
import random

data_directory = "../data/"
data_file = "accounts.json"
# accounts = ["id","accounts_number", "balance", "inspect_button", ["operation_list"]]

def random_number(digits): # Creates every number of the accounts number randomly
    number_string = ""
    for i in range(digits):
        number_string += str(random.randint(0,9))

    return number_string

def accounts_number_random(): # Creates the accounts number calling random_number
    return f"ES{random_number(2)} {random_number(4)} {random_number(4)} {random_number(2)} {random_number(9)}"

def get_id():
    counter = 1
    if os.path.getsize(data_directory+data_file) != 0:
        file = open(data_directory+data_file)
        accounts_temp = json.load(file)
        for account in accounts_temp:
            counter += 1
    return counter

def create_account():
    return [get_id(), accounts_number_random(), 0.0, f"<a href='check_account.py?id={get_id()}'><button>Check Account</button></a>", []]

if os.path.getsize(data_directory+data_file) == 0:
    accounts = [create_account()]
else:
    file = open(data_directory+data_file)
    accounts = json.load(file)
    accounts.append(create_account())

accounts_parse_json = json.dumps(accounts)
file = open(data_directory+data_file,"wt")
file.write(accounts_parse_json)
file.close()
atm_GUI.operation_done()