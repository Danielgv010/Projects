#!C:\Users\zx22student3206\AppData\Local\Programs\Python\Python311\python.exe

print("Content-type: text/html\n")

import htmlPages
import http.cookies, os

if os.environ.get("HTTP_COOKIE") == None:
    htmlPages.info_page("error","You're not logged in","../index.html")
    exit()

cookie = http.cookies.SimpleCookie()
cookie.load(os.environ.get("HTTP_COOKIE"))

if "LOGIN" in cookie:
    htmlPages.application("Page 2","Page 1","page1.py")
else:
    htmlPages.info_page("error","You're not logged in","../index.html")