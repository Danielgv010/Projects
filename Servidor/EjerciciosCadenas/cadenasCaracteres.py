#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
param = parse_qs(parsed_url[4])

#Contiene el texto introducido en el formulario por el usuario
texto = param["texto"][0]
palabra = param["palabra"][0]
letra = param["letra"][0]

#Genera el inicio de un HTML
def inicioHTML():
    print("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Ejercicios de cadenas de caracteres</title>
        </head>
        <body>
    """)

#Genera el final de un HTML
def finHTML():
    print("""
        </body>
        </html>
    """)

#Separa las letras en diferentes líneas
def separaLetrasLineas(texto):
    for i in texto:
        print(i+"<br>")

#Cuenta las letras de una frase sin contar los espacios o caracteres no alfanumericos
def cuentaLetras(texto):
    contador = 0
    for i in texto.upper():
        if i >= "A" and i <= "Z" or i == "Ñ":
            contador+=1
    print(contador)

#Le da la vuelta al string (mirror)
def vueltaFrase(texto):
    print(texto[::-1])

#Comprueba que la palabra envíada por el usuario esté en el texto que también envió
def contienePalabra(texto,palabra):
    return palabra in texto

#Devuelve el numero de veces que aparece la letra en el texto, en caso de error devuelve -1
def contarLetra(texto,letra):
    contador = 0
    if len(letra) == 1:
        for l in texto:
            if (letra == l):
                contador += 1
    else:
        contador = -1
    return contador

#Centa cuantas vocales hay en el texto
def contarVocales(texto):
    a=0
    e=0
    i=0
    o=0
    u=0
    for l in texto:
        match l.lower():
            case "a":
                a+=1
            case "e":
                e+=1
            case "i":
                i+=1
            case "o":
                o+=1
            case "u":
                u+=1

    print(f"Hay {a} as, {e} es, {i} is, {o} os y {u} us")

def dividirPalabras(texto):
    return texto.split(" ")



#Salida que se envía al cliente
inicioHTML()
separaLetrasLineas(texto)
print("<hr>")
cuentaLetras(texto)
print("<hr>")
vueltaFrase(texto)
print("<hr>")
if contienePalabra(texto,palabra):
    print("Palabra encontrada")
else:
    print("Palabra no encontrada")
print("<hr>")
print(contarLetra(texto,letra))
print("<hr>")
contarVocales(texto)
print("<hr>")
print(dividirPalabras(texto))
finHTML()