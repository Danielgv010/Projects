#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos
import FormVideojuegos

print("Content-type: text/html\n")

bd = BDVideoJuegos()
HtmlVideoJuegos.salidaPrincipal(
    bd.juegosConFiltro(FormVideojuegos.crearFiltros()))
bd.cerrarBD()
