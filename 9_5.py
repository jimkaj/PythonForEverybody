# Ex 9.5: Record domain names.  Print domains & frequency

# open file
inp = input('Enter file name: ')
try: fhand = open(inp)
except:
    print("Can't find file ",inp)
    quit()
    
#count domains
domains = {}
for lines in fhand:
    if not lines.startswith('From '): continue
    words = lines.split()
    email = words[1]
    cuplet = email.split('@')
    domain = cuplet[1]
    if domain not in domains:
        domains[domain] = 1
    else:
        domains[domain] += 1

#print domains and counts
print(domains)
    