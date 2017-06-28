# Ex 10.1: Read file for emails. Count messages from each. 

# Open File
inp = input('Enter a file name: ') #Use mbox-short.txt or mbox.txt
try: fhand = open(inp)
except:
    print("Can't find file ",inp)
    quit()
    
# read and count emails
d = dict()
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    if email not in d:
        d[email] = 1
    else:
        d[email] += 1

# sort emails 
lst = list()
for mail,count in d.items():
    lst.append ((count,mail))
lst.sort(reverse=True)
tcount, temail = lst[0]
print('Top email is',temail,'with a total of ', tcount,'emails.')

#save to file
fout = open('emails.txt','w')
for count,mail in lst:
#    line = str()
#    line = mail + '\t' + str(count) + '\n'
#    fout.write(line)
    fout.write((mail + '\t' + str(count) + '\n')) #shorter version of 3 lines above
fout.close()

  