#experiment with files
fhand = open('mbox.txt')
print(fhand)
mout = open('email.txt','w')

# Finds e-mails and writes to file
for line in fhand:
    if line.startswith('From: '):
        line = line.rstrip()
        mail = line[6:] + '\n'
        mout.write(mail)
mout.close()
fhand.close()
        
        
       