#!/usr/bin/env python3
import cgi, cgitb, secret, os, templates

form = cgi.FieldStorage()

username = form.getvalue('username') 
password = form.getvalue('password')

# Q4 
# print("Content-Type: text/html\r\n\r\n")
# print("<!doctype html><html><head><title>CMPUT404 cgi lab</title></head><body>")
# print(f"Username: {username}</p> <p>Password: {password}</p>")

if(os.environ.get('HTTP_COOKIE').startswith('authenticated')):
    print("Content-Type: text/html\r\n\r\n")
    print("<!doctype html><html><head><title>CMPUT404 cgi lab</title></head><body>")
    print(templates.secret_page(secret.username, secret.password))
else:
    if(username == secret.username and password == secret.password):
        # set cooklie 
        print("Set-Cookie: authenticated=True")

        # display secret page
        print("Content-Type: text/html\r\n\r\n")
        print("<!doctype html><html><head><title>CMPUT404 cgi lab</title></head><body>")
        print(templates.secret_page(username, password))
    else:
        print("Content-Type: text/html\r\n\r\n")
        print("<!doctype html><html><head><title>CMPUT404 cgi lab</title></head><body>")
        print("Incorrect!!")

print("</body></html>")