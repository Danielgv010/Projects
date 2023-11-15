#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos
import FormVideojuegos

print("Content-type: text/html\n")

bd = BDVideoJuegos()
HtmlVideoJuegos.salidaPrincipal(
    bd.juegosConFiltro(FormVideojuegos.crearFiltros()))
bd.cerrarBD()
