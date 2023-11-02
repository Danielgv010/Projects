#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

import cgi ,os, csv
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
first_row = True

print("Content-type: text/html\n")

file_item = form["file-name"] # Pilla el archivo subido en el formulario

if file_item.filename: # Comprueba que se halla seleccionado un fichero
    file_name = os.path.basename(file_item.filename) # Extrae el nombre del fichero de la ruta
    open(f"ficheros/{file_name}","wb").write(file_item.file.read()) # Abre el fichero en modeo escritura y copia la informacion del archivo subido en el formulario en el archivo que acaba de abrir


    print("<table border='1' style='border-collapse:collapse;'>") # Crea el inicio de la tabla
    with open(f'ficheros/{file_name}', 'r') as file: # Abre el fichero en modo lectura
        reader = csv.reader(file) # Abre el fichero con un lector de csv y pone los contenidos en la variable

        for row in reader: # Por cada fila de la lista reader
            splitted_row = row[0].split(";") # Separa los valores en una lista, partiendo por el ;
            print("<tr>") # Crea el inicio de una fila de la tabla

            for value in splitted_row: # Por cada valor en la fila
                if (first_row): # Si es la primera fila
                    print(f"<th>{value}</th>") # Crea un th con el valor
                else:
                    print(f"<td>{value}</td>") # Crea un td con el valor
            first_row=False # Indica que la primera fila ya se ha escrito

            print("</tr>") # Cierra la fila de la tabla
    print("</table>") # Cierra la tabla