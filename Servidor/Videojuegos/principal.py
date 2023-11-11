#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from BDvideojuegos import BDVideoJuegos
import HtmlVideoJuegos, sys

print("Content-type: text/html\n")

print(sys.executable)

bd = BDVideoJuegos()
HtmlVideoJuegos.salidaPrincipal(bd.todosLosVideojuegos())
bd.cerrarBD()
