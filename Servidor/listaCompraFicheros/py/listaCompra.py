#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import codigoHtml, os

def listar_productos(): #Crea una lista ordenada con los productos
    if len(productos) != 0: #Si hay productos se crea la lista
        print("<ol>")
        #Antes de poner cada elemento se quita el enter
        for producto in [producto.strip('\n') for producto in productos]:
            #Separa el elemento por el ; para tener el producto y la cantidad en un array
            elemento = producto.split(";")
            #Da formato al imprimir el elemento en la lista
            print(f"<li>{elemento[1]} de {elemento[0]}</li>")
        print("</ol>")
    else: #Si la lista no tiene productos
        print("<h2>La lista de la compra esta vacia</h2>")

try:
    #Abrir el fichero en modo lectura
    fichero = open("../datos/listaCompra.dat")
except:
    #Se crea el fichero en datos si da error al abrir
    fichero = open("../datos/listaCompra.dat","x")

if os.path.getsize("../datos/listaCompra.dat") != 0: #Si el fichero no esta vacio
    #Leemos el contenido del fichero en una lista de productos
    productos = fichero.readlines()
else: #Si el fichero esta vacio
    productos = []

#Cerramos el fichero
fichero.close()

#Creamos el inicio del HTML
codigoHtml.inicio_cesta_compra()

#Crear la lista de productos
listar_productos()
print("<hr>")

codigoHtml.formulario()
#Creamos el final del HTML
codigoHtml.fin_cesta_compra()
