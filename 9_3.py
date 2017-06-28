# Ex 9.7: categorize e-mails by day of week
inp = input('Enter a file name: ') # use mbox-short.txt
try: fhand = open(inp)
except: 
    print('Cannot find file ',inp)
    quit()

daycount = {}
for lin in fhand:
    if not lin.startswith('From '): continue
    words = lin.split()
    if words[2] not in daycount: #Word[2] is day of week email sent
        daycount[words[2]] = 1
    else: 
        daycount[words[2]] += 1
        
print(daycount)
    