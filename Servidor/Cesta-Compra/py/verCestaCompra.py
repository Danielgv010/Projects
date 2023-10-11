#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies
import os
import funcionesHTML

print("Content-Type: text/html\n")
cookie = http.cookies.SimpleCookie()

teclados = 0
ratones = 0
monitores = 0

if os.environ.get("HTTP_COOKIE") != None:
    cookie.load(os.environ.get("HTTP_COOKIE"))
    if "teclado" in cookie:
        teclados = cookie["teclado"].value
    if "raton" in cookie:
        ratones = cookie["raton"].value
    if "monitor" in cookie:
        monitores = cookie["monitor"].value

print(f"teclados:{teclados} ratones:{ratones} monitores:{monitores}")