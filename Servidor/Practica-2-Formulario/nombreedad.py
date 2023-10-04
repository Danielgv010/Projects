#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import os
from urllib.parse import urlparse, unquote, parse_qs

print("""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Document</title>
        </head>
        <body>
        <h1>Tratar formularios</h1>
""")

ru = os.environ.get("REQUEST_URI")
parsed_url = urlparse(ru)
parameters = parse_qs(parsed_url[4])
print(parameters["nombre"][0])
print(parameters["edad"][0])


print("""
    </body>
    </html>
""")