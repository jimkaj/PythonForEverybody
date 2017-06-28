# Ex 9.4: count messages from each person.  Find max

# open file
inp = input('Enter file name: ') # use mbox-short.txt
try: fhand = open(inp)
except:
    print("Can't find file ",inp)
    quit()

# count e-mails from each address
sender = {}    
for lin in fhand: 
        if not lin.startswith('From '): continue
        words = lin.split()
        if words[1] not in sender:
            sender[words[1]] = 1
        else:
            sender[words[1]] += 1
            
#Find max count
lst = list(sender.values())
lst.sort()
lst.reverse()
hi = lst[0]

#print e-mails == max value
for key in sender:
    if sender[key] == hi:
        print(key, sender[key])  
