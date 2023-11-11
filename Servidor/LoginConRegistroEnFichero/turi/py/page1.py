#!C:\Users\deras\AppData\Local\Programs\Python\Python310\python.exe

print("Content-type: text/html\n")

import htmlPages
import http.cookies, os

if os.environ.get("HTTP_COOKIE") == None:
    htmlPages.info_page("error","You're not logged in","../index.html")
    exit()

cookie = http.cookies.SimpleCookie()
cookie.load(os.environ.get("HTTP_COOKIE"))

if "LOGIN" in cookie:
    htmlPages.application("Page 1","Page 2","page2.py")
else:
    htmlPages.info_page("error","You're not logged in","../index.html")