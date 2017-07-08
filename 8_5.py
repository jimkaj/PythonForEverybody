# Ex 8.5: print e-mails & count
inp = input('Enter a file: ') # use mbox-short.txt
try: fhand = open(inp)
except: 
    print("Can't find file ",inp)
    quit()
count = 0
for line in fhand:
    if not line.startswith('From'): continue
    words = line.split()
    print(words[1])
    count = count +1
print('There are ',count,' from lines.')
            