#!C:\Users\Prince Johnson\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\python.exe

import os
import sys
import cgi
import cgitb

print("Content-type: text/html\n")
cgitb.enable()
form = cgi.FieldStorage()
name = form.getvalue('name')
mail = form.getvalue('email')
password = form.getvalue('password')
emotions  = form.getlist('emotions')
