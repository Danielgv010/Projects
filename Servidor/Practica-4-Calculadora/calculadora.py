#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os 
from urllib.parse import urlparse, unquote, parse_qs
#from urllib.parse import parse_qs

#param = parse_qs(os.environ.get("QUERY STRING"))
ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
parameters = parse_qs(parsed_url[4])

n1 = int(parameters["num1"][0])
n2 = int(parameters["num2"][0])
oper = parameters["operacion"][0]

"""
salida = "El resultado de la {} de {} {} {} es {}"

if oper == "s:
    print(salida.format("suma",n1,"mas",n2,n1+n2))
if oper == "r":
    print(salida.format("resta",n1,"menos",n2,n1-n2))
if oper == "m":
    print(salida.format("mutiplicación",n1,"por",n2,n1*n2))
if oper == "d":
    print(salida.format("división",n1,"entre",n2,n1/n2))
"""
match oper:
    case "s":
        print(n1+n2)
    case "r":
        print(n1-n2)
    case "m":
        print(n1*n2)
    case "d":
        print(n1/n2)
