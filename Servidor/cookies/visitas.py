#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies
import os

def htmlEntrada():
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Cookies</h1>
    """)
def htmlFin():
    print("""
        </body>
    </html>
    """)

#Comprobar si el cliente nos envía la cookie CONTADOR
#Si es true -> incrementamos el valor que trae la cookie CONTADOR
#Si es false -> CONTADOR = 1

print("Content-Type: text/html")
cookie = http.cookies.SimpleCookie()

cookie["cuqui"] = "rushB"

def crearCookie():
    cookie["CONTADOR"] = 1
    cookie["CONTADOR"]["expires"] = "Wed, 11 Oct 2024 07:30:00 GMT;"
    print(cookie)
    print()


if os.environ.get("HTTP_COOKIE") == None:
    crearCookie()
else:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "CONTADOR" in cookie:
        cookie["CONTADOR"] = int(cookie["CONTADOR"].value) + 1
        cookie["CONTADOR"]["expires"] = "Wed, 11 Oct 2024 07:30:00 GMT;"
        print(cookie)
        print()
    else:
        crearCookie()

#Codigo html que se envía al navegador
htmlEntrada()
print("<h3>"+cookie["CONTADOR"].value+"</h3>")
print("<a href='borrarcookie.py'>Borrar cookie</a>")
htmlFin()
