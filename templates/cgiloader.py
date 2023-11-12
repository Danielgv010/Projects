
# Este python permite tratar los ficheros subidos por el usuario en un formulario
# Si se va a usar este .py el form necesita tener enctype="multipart/form-data" y method="post" como atributos

import cgi ,os
import cgitb; cgitb.enable()


# -------- Recibe como parámetros el nombre del directorio a comprobar --------

def directory_exists(directory): # Comprueba que el directorio donde se guardará el archivo existe y si no existe lo crea
    if not os.path.isdir(directory): # Si no existe la carpeta, la crea
        os.mkdir(directory)


# -------- Recibe como parámetros el nombre del input donde se sube el archivo y el directorio donde se quiere guardar el archivo --------

def save_file(file_selector_name, file_directory): # Hace una copia del archivo subido por el usuario en el directorio que se le indica a la funcion y devuelve el nombre del fichero
    directory_exists(file_directory)  # Comprueba que el directorio donde se guardará el archivo existe
    form = cgi.FieldStorage() # Crea un objeto cgi
    file_item = form[file_selector_name] # Pilla el archivo subido en el formulario
    if file_item.filename: # Comprueba que se haya seleccionado un fichero
        file_name = os.path.basename(file_item.filename) # Extrae el nombre del fichero de la ruta
        open(f"{file_directory}{file_name}","wb").write(file_item.file.read()) # Copia el fichero subido por el usuario en un directorio local con el mismo nombre
    return file_name


# -------- Recibe como parámetros el directorio donde se encuentra el archivo a procesar, el nombre de dicho archivo y el carácter con el que se hará el split() --------

def create_table(file_directory, file_name, separator): # Devuelve una tabla con los datos del fichero y la devuelve
    table = "<table border='1px solid'>"
    with open(file_directory+file_name) as file: # Abre el fichero en modo lectura
        header = file.readline().split(separator) # Hace un array separando la primera linea del fichero por el separador que se le pasa a la funcion
        header = [element.strip() for element in header] # Elimina los espacios vacíos de los valores del array
        table += "<tr>"
        for value in header: # Por cada valor del array header crea los th de la tabla
            table += f"<th>{value}</th>"
        table += "</tr>"
        for line in file: # Por cada linea restante en el fichero
            table += "<tr>"
            for data in line.split(separator): # Hace un array separando la primera linea del fichero por el separador que se le pasa a la funcion y lo recorre para crear los td
                table += f"<td>{data.strip()}</td>"
            table += "<tr>"
        table += "</table>"
        return table


# -------- Recibe como parámetros el directorio donde se encuentra el archivo a procesar, el nombre de dicho archivo y el carácter con el que se hará el split() --------

def create_list(file_directory, file_name, separator): # Crea una lista html con los atos del fichero y la devuelve
    list = "<ol>"
    with open(file_directory+file_name) as file: # Abre el fichero en modo lectura
        for i, value in enumerate(file.read().split(separator)): # Lee el fichero, lo mete en un array separandolo por el separator pasado a la funcion y recorre el array almacenando el número de iteración en i
            if i == 0: # Si es la primera iteracion del for crea un h1
                list += f"<h1>{value}</h1>"
            else: # Si no es la primera iteracion crea un li
                list += f"<li>{value}</li>"
    list += "</ol>"
    return list
