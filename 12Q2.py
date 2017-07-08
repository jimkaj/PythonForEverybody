# Chapter 12 Quiz #2; James Kadjasz
# This runs on Python 3.x 

# To install BeautifulSoup:: 
# To add PIP commands to CMD prompt, you have to add 
# folder of python scripts to the operating environment
# in CMD: setx PATH "%PATH%;C:\Users\<<full path here>>\Python35-32\Scripts"
# then run in new CMD window prompt: "pip install beautifulsoup4"

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSLdir certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter inputs
url = input('Enter - ')
#url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count: ')) # how many pages do you want to scan?
pos = int(input('Enter position: ')) # what link on page do you follow?

# Retrieve anchor tag from the [pos] for (count) pages
while count > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    ptag = tags[(pos-1)] #tag at position[pos]
    nlink = ptag.get('href', None) #next link
    print(nlink)
    url = nlink
    count = count -1
print('Done!')    

