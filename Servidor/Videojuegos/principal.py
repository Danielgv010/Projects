#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos

print("Content-type: text/html\n")

bd = BDVideoJuegos()
HtmlVideoJuegos.salidaPrincipal(bd.todosLosVideojuegos())
bd.cerrarBD()
