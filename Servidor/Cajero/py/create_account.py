#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import json
import random

data_directory = "../data/"
data_file = "accounts.json"
# account = ["id","account_number", "balance", "inspect_button", ["operation_list"]]

def random_number(numbers): # Creates every number of the account number randomly
    number_string = ""
    for i in range(numbers):
        number_string += str(random.randint(0,9))

    return number_string

def account_number_random(): # Creates the account number calling random_number
    return f"ES{random_number(2)} {random_number(4)} {random_number(4)} {random_number(2)} {random_number(9)}"

def open_and_write_file():
    file = open(data_directory+data_file+"at")
    account = [1, account_number_random(), 0.0, "button", ["deposit", "deposit"]]
    account_parse_json = json.dumps(account)
    file.write(account_parse_json)
    file.close()
