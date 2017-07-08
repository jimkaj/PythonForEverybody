# Ex 12.1: Change 
import urllib

fhand = urlib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print line.strip()