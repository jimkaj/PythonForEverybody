# James Kajdasz Answer for Chapter 13, Quiz #1
#Runs on Python 3.X
# extract .xml data and add up 'comment' numbers

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSLdir certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Get web page info
#url = 'http://python-data.dr-chuck.net/comments_42.xml'
url = 'http://python-data.dr-chuck.net/comments_246502.xml'
#url = input('Enter Location: ')
xml = urllib.request.urlopen(url, context=ctx).read() #web page into single str
print('Retrieved',len(xml),'characters') 

#Parse xml format of web page info
tree = ET.fromstring(xml) #extracts tree structure of xml
lst = tree.findall('.//comment') #puts count items in list
print('Count:', len(lst)) #Num of count items

#Total up counts
total = 0
for item in lst: 
    total = total + int(item.find('count').text)
print('Sum: ',total)