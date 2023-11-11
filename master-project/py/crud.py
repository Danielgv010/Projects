#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

print("Content-type: text/html\n")

import htmlCode
from DBmanager import DBmanager

database = DBmanager()
htmlCode.crud(database.list_all())
database.close_database()