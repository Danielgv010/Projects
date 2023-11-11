#!C:\Users\deras\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

from DBmanager import DBmanager
from urllib.parse import parse_qs
import os, htmlCode

# Obtener los parametros que envía el formulario
parameter = parse_qs(os.environ.get('QUERY_STRING'))

if 'name' not in parameter:
    htmlCode.message_page('error','Fields cant be empty','crud.py')
    exit()
if 'company' not in parameter:
    htmlCode.message_page('error','Fields cant be empty','crud.py')
    exit()
if 'theme' not in parameter:
    htmlCode.message_page('error','Fields cant be empty','crud.py')
    exit()
if 'player-count' not in parameter:
    htmlCode.message_page('error','Fields cant be empty','crud.py')
    exit()
if 'release-date' not in parameter:
    htmlCode.message_page('error','Fields cant be empty','crud.py')
    exit()

name = parameter['name'][0]
company = parameter['company'][0]
theme = parameter['theme'][0]
player_count = parameter['player-count'][0]
release_date = parameter['release-date'][0]

if name == '' or company == '' or theme == '' or player_count == '' or release_date == '':
    htmlCode.message_page('error','Fields cant be empty','crud.py')
    exit()


database = DBmanager()
database.insert_row(name,company,theme,player_count,release_date)
htmlCode.message_page('success','Row inserted','crud.py')
database.close_database()