
# Este python permite gestionar cookies

import http.cookies
import os


def get_cookies(): # Devuelve una lista con las cookies activas
    return os.environ.get("HTTP_COOKIE")


# -------- Recibe como parámetros el nombre de la cookie a comprobar --------

def check_cookie_existence(cookie_name): # Comprueba que la cookie con el nombre que se le pasa a la funcion exista en la lista de cookies activas, devolviendo true o false
    cookie = http.cookies.SimpleCookie()
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    return cookie_name in cookie


# -------- Recibe como parámetros el objeto cookie a imprimir --------

def print_cookie(cookie): # Imprime la cookie
    print("Content-type: text/html")
    print(cookie)
    print()


# -------- Recibe como parámetros en nombre de la cookie, el valor de la cookie y la fecha de exipración de la cookie --------
# -------- La fecha de expiración de la cookie es opcional. Si no se quiere incluir, se pone un 0 --------

def create_cookie(cookie_name, cookie_value, cookie_expiration): # Crea una cookie con los valores que se le pasan
    cookie = http.cookies.SimpleCookie()
    cookie[cookie_name] = cookie_value # Le asigna un nombre y un valor a la cookie
    if cookie_expiration != 0: # Si se añade una fecha de expiración a los parámetros de la funcion
        cookie[cookie_name]["expires"] = cookie_expiration
    print_cookie(cookie) # Imprime la cookie


# -------- Recibe como parámetros el nombre de la cookie a borrar --------

def delete_cookie(cookie_name): # Borra la cookie que se le indique a la funcion
    cookie = http.cookies.SimpleCookie()
    cookie[cookie_name] = 1 # Le asigna un valor a la cookie
    cookie[cookie_name]["expires"] = "Fri, 10 Oct 2023 07:30:00 GMT;" # Añade una fecha de expiración anterior a la fecha actual para que se borre la cookie
    print_cookie(cookie) # Imprime la cookie


# -------- Recibe como parámetros el nombre de la cookie a actualizar y el nuevo valor de la misma aparte de la nueva fecha de expiración --------

def update_cookie(cookie_name, cookie_value, cookie_expiration): # Modifica el valor y la expiración de la cookie
    cookie = http.cookies.SimpleCookie()
    cookie[cookie_name] = cookie_value # Asigna el nuevo valor a la cookie
    cookie[cookie_name]["expires"] = cookie_expiration # Asigna la nueva fecha de expiracion a la cookie
    print_cookie(cookie) # Imprime la cookie


# -------- Recibe como parámetros el nombre de la cookie a actualizar y el nuevo valor de la misma --------

def update_cookie_value(cookie_name, cookie_value): # Modifica el valor de la cookie
    cookie = http.cookies.SimpleCookie()
    cookie[cookie_name] = cookie_value # Asigna el nuevo valor a la cookie
    print_cookie(cookie) # Imprime la cookie


# -------- Recibe como parámetros el nombre de la cookie a actualizar y la nueva fecha de expiración --------

def update_cookie_expiration(cookie_name, cookie_expiration): # Modifica el valor de expiracion de la cookie
    cookie = http.cookies.SimpleCookie()
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    cookie[cookie_name] = cookie[cookie_name].value # Asigna el mismo valor a la cookie
    cookie[cookie_name]["expires"] = cookie_expiration # Asigna la nueva fecha de expiracion a la cookie
    print_cookie(cookie) # Imprime la cookie


# -------- Recibe como parámetros el nombre de la cookie que se quiere comprobar el valor --------

def get_cookie_value(cookie_name): # Devuelve el valor de la cookie con el nombre que se le pasa a la funcion
    cookie = http.cookies.SimpleCookie()
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    return cookie[cookie_name].value


# -------- Recibe como parámetros el nombre de la cookie sobre la que operar, el tipo de operación a realizar y el numero de incremento/decremento --------
# -------- Solo acepta + si se quiere incrementar o - si se quiere decrementar --------

def counter_cookie(cookie_name, operator, value): # Incrementa o decrementa el valor de una cookie
    cookie = http.cookies.SimpleCookie()
    cookie.load(get_cookies()) # Carga las cookies activas en el objeto cookie
    if operator == "+": # Si se quiere incrementar el valor de la cookie
            cookie[cookie_name] = int(cookie[cookie_name].value) + value
    elif operator == "-": # Si se quiere decrementar el valor de la cookie
            cookie[cookie_name] = int(cookie[cookie_name].value) - value
    print_cookie(cookie) # Imprime la cookie

