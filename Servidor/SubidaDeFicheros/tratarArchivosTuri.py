#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import cgi ,os
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

def create_table(file_name):
    print("Content-Type: text/html\n")
    print("<table border='1px solid'>")

    with open(file_name) as file:
        header = file.readline().split(";")

        header = [element.strip() for element in header]

        print("<tr>")
        for data in header:
            print(f"<th>{data}</th>")
        print("</tr>")

        for line in file:
            print("<tr>")
            for data in line.split(";"):
                print(f"<td>{data.strip()}</td>")
            print("</tr>")
        print("</table>")


file_item = form["file-name"] # Pilla el archivo subido en el formulario

if file_item.filename: # Comprueba que se halla seleccionado un fichero
    file_name = os.path.basename(file_item.filename) # Extrae el nombre del fichero de la ruta
    open(f"ficheros/{file_name}","wb").write(file_item.file.read())
    create_table(file_name)

