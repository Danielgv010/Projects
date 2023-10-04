#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

print("""
<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Document</title>
        </head>
        <body>
            <h1>Hello World!!</h1>
        </body>
    </html>
""")

#en la configuracion del apache, click derecho, httpd confg, buscamos addhandler, y en el segundo
#donde estan las extensiones, añadimos .py (AddHandler cgi-script .cgi .pl .asp .py)