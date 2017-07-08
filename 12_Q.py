# Quiz1 for Chapter 12
# This runs in Python 3.X
# count up numbers inside 'span' tag and total up

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSLdir certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
url = 'http://python-data.dr-chuck.net/comments_246505.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the <span> tags, parse number, add to total
spans = soup('span')  #Retrieves data with <span> tag
total = 0
for s in spans:
    n = int(s.contents[0]) #extract content from 'span' tag
    total = total + n
print(total)
