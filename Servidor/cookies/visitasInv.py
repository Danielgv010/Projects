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

def crearCookie():
    cookie["DESCONTADOR"] = 10
    print(cookie)
    print()

if os.environ.get("HTTP_COOKIE") == None or "DESCONTADOR" not in os.environ.get("HTTP_COOKIE"):
    crearCookie()
else:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if int(cookie["DESCONTADOR"].value) != 0:
        cookie["DESCONTADOR"] = int(cookie["DESCONTADOR"].value) - 1
        print(cookie)
        print()

htmlEntrada()
print("<h3>"+cookie["DESCONTADOR"].value+"</h3>")
htmlFin()