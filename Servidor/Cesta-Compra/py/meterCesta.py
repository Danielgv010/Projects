#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import http.cookies
import os
import funcionesHTML

from urllib.parse import urlparse, unquote, parse_qs
import math

#Recupera las variables del sistema
ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
#Extrae los valores del form de las variables del sistema
parameters = parse_qs(parsed_url[4])

prod = 0

#Si hay "prod" en la url a partir del ? coge el valor de "prod"
if "prod" in parameters:
    prod = int(parameters["prod"][0])

print("Content-Type: text/html")
cookie = http.cookies.SimpleCookie()

def imprimirCookie(): #Imprime la cookie en el navegadro
    print(cookie)
    print()

def crearCookie(nombre): #Crea una cookie con el nombre que se le pase como valor
    cookie[nombre] = 1
    cookie[nombre]["expires"] = "Wed, 11 Oct 2024 07:30:00 GMT;"
    imprimirCookie()

def incrementarCookie(nombre): #Incrementa el valor de la cookie que se le pase como valor en 1
    cookie[nombre] = int(cookie[nombre].value) + 1

#Comprueba que cookie tiene que crear/modificar
match prod:
    case 0: #Indica que no se ha pulsado nada
        pass
    case 1: #Indica que se quiere crear/modificar la cookie de "teclado"
        #Comprueba que haya cookies, si no hay crea la cookie de "teclado"
        if os.environ.get("HTTP_COOKIE") == None:
            crearCookie("teclado")
        else:
            cookie.load(os.environ.get("HTTP_COOKIE"))
            #Si hay cookies pero no la cookie "teclado", la crea
            if "teclado" not in cookie:
                crearCookie("teclado")
            else:
                #Si la cookie "teclado" existe, la incrementa en 1
                incrementarCookie("teclado")
                imprimirCookie()
    case 2: #Indica que se quiere crear/modificar la cookie de "raton"
        #Comprueba que haya cookies, si no hay crea la cookie de "raton"
        if os.environ.get("HTTP_COOKIE") == None:
            crearCookie("raton")
        else:
            cookie.load(os.environ.get("HTTP_COOKIE"))
            #Si hay cookies pero no la cookie "raton", la crea
            if "raton" not in cookie:
                crearCookie("raton")
            else:
                #Si la cookie "raton" existe, la incrementa en 1
                incrementarCookie("raton")
                imprimirCookie()
    case 3: #Indica que se quiere crear/modificar la cookie de "monitor"
        #Comprueba que haya cookies, si no hay crea la cookie de "monitor"
        if os.environ.get("HTTP_COOKIE") == None:
            crearCookie("monitor")
        else:
            cookie.load(os.environ.get("HTTP_COOKIE"))
            #Si hay cookies pero no la cookie "monitor", la crea
            if "monitor" not in cookie:
                crearCookie("monitor")
            else:
                #Si la cookie "monitor" existe, la incrementa en 1
                incrementarCookie("monitor")
                imprimirCookie()

#Genera el html
funcionesHTML.pagPrincipal()