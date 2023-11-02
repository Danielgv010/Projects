#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import cgi ,os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

def create_list(file_name): # Crea la lista
    print("Content-Type: text/html\n") # Declaración del tipo de contenido

    print("<ol>") # Inicio de la lista
    with open(file_name) as file: # Abre el fichero en modo lectura
        for i, value in enumerate(file.read().split(",")): # Lee el fichero, lo mete en un array separandolo por , y recorre el array almacenando el número de iteración en i
            print(f"<h1>{value}</h1>") if i==0 else print(f"<li>{value}</li>") # Si es la primera iteración hace un h1, de no ser la primera iteración hace un li
    print("</ol>") # Fin de la lista


file_item = form["file-name"] # Pilla el archivo subido en el formulario

if file_item.filename: # Comprueba que se halla seleccionado un fichero
    file_name = os.path.basename(file_item.filename) # Extrae el nombre del fichero de la ruta
    open(f"ficheros/{file_name}","wb").write(file_item.file.read()) # Abre un fichero en modo escritura y le copia el contenido del fichero subido por el usuario
    create_list(f"ficheros/{file_name}") # Crea la lista