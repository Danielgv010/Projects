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

print("Content-Type: text/html")
cookie = http.cookies.SimpleCookie()
cookie["CONTADOR"] = 1
#Para borrar la cokie instantaneamente hay que poner una fecha anterior a la fecha en la que estemos
#Es debido a que estás editando la fecha de expiración de la cookie
cookie["CONTADOR"]["expires"] = "Wed, 11 Oct 2022 07:30:00 GMT;"
print(cookie)
print()

#Codigo html que se envía al navegador
htmlEntrada()
print("<h3>Cookie Borrada</h3>")
print("<a href='borrarcookie.py'>Borrar cookie</a>")
htmlFin()
