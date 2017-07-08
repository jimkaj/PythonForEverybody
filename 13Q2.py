# James Kajdasz
# Chapter 13 Quiz #2: Extracting data from JSON
# Runs on Python 3.X
#The program will prompt for a URL, read the JSON 
#data from that URL using urllib and then parse and 
#extract the comment counts from the JSON data, compute 
#the sum of the numbers in the file
#The desired info is in a dict inside a list inside a dict :0

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSLdir certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
    
#Query for URL
#url = 'http://python-data.dr-chuck.net/comments_42.json'
url = 'http://python-data.dr-chuck.net/comments_246506.json'
#url = input('Enter URL: ')

#Get info from URL
print('Retrieving ',url)
inp = urllib.request.urlopen(url, context=ctx).read() #Open page
inps = bytes.decode(inp)  #converts bytes to str

#parse json
info = json.loads(inps) # parses json string into dict w/ 2 keys
lst = (info['comments']) # takes 2nd key from dict, which is a list
print('User count:', len(lst))

#total up 
total = 0
for items in lst: #work through dict(items) in list and extract number
    num = items['count']
    total = total + num
print('Total is: ',total)


