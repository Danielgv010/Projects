#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from DBmanager import DBmanager
from urllib.parse import parse_qs
import os, htmlCode

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

if parameter["id"][0] != "":
    database = DBmanager()
    database.delete(parameter["id"][0])
    htmlCode.message_page("success","row deleted","crud.py")
    database.close_database()
else:
    htmlCode.message_page("error","No id was provided","crud.py")