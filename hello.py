#!/usr/bin/env python3
import os, json, cgi, cgitb, templates

print("Content-Type: text/html\r\n\r\n")
print("<!doctype html><html><head><title>CMPUT404 cgi lab</title></head><body>")

# Q1 
print(os.environ)
json_object = json.dumps(dict(os.environ), indent = 4)
print(json_object)

# Q2 
for param in os.environ.keys():
    if(param == "QUERY_STRING"):
        print(f"<em>param</em> = {os.environ[param]}")   

# Q3 
for param in os.environ.keys():
    if(param == "HTTP_USER_AGENT"):
        print(f"<em>param</em> = {os.environ[param]}")   

cgitb.enable()
print(templates.login_page())

print("</body></html>")