# Python for Informatics
# Ex 10.2: counts distribution of hours of day emails sent

# open file
inp = input('Enter file name: ') #Enter a text file
try: fhand = open(inp)
except:
    print("can't find file ",inp)
    quit()

# read hour and count into dict
hours = dict()
print('Working... This may take a minute.')
for line in fhand:
    if not line.startswith('From '): continue
    else:
        #find hour
        words = line.split()
        time = words[5]
        ptime = time.split(':')
        hour = ptime[0]
        # write hour into dictionary w/ counts
        if hour not in hours: hours[hour] = 1
        else: hours[hour] += 1

#sort hours
lst = list()
for hour, count in hours.items():
    lst.append((int(hour), count))
lst.sort()

# Output to File
fout = open('output.txt','w')
fout.write('Hour' + '\t' + 'Count' + '\n') 
print('Hour ','Count')
for hour,count in lst:
    fout.write((str(hour) + '\t' + str(count) + '\n'))
    print(hour,'\t',int(count))
fout.close()   
    