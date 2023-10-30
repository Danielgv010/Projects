#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html")

import htmlPages
import http.cookies

cookie = http.cookies.SimpleCookie()
cookie["LOGIN"] = 1
cookie["LOGIN"]["expires"] = "Mon, 30 Oct 2023 00:00:00 GMT"

print("Content-Type: text/html")
print(cookie["LOGIN"])
print()

htmlPages.info_page("success","Logging out...","../index.html")