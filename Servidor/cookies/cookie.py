#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies
import os
from urllib.parse import urlparse, unquote, parse_qs


# Recupera las variables del sistema
ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
# Extrae los valores del form de las variables del sistema
parameters = parse_qs(parsed_url[4])

usuario = parameters["usuario"][0]
password = parameters["password"][0]

dentro = False

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
        <h1>Estas dentro</h1>
    </body>
    </html>F
    """)


def htmlError():
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
    <h3>ERROR EN LA AUTENTICACION</h3>
    <form action="cookie.py" method="get">
        <label for="usuario">Usuario</label>
        <input type="text" name="usuario" id="usuario">
        <label for="password">Password</label>
        <input type="password" name="password" id="password">
        <input type="submit" value="submit">
    </form>
    </body>
    </html>
    """)

if (usuario == "pepe") and (password == "1234"):
    dentro = True

if not dentro:
    print("Content-type: text/html\n")
    htmlError()
else:
    print("Content-type: text/html")
    cookie = http.cookies.SimpleCookie()
    cookie["ID1"] = "ALGO"

    print(cookie)
    print()
    htmlEntrada()


