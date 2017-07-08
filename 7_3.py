# Ex 7.3: Count lines w/ easter egg
inp = input('Enter the file name: ')
if inp == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
try: fhand = open(inp)
except:
    print('File cannot be opened: ',inp)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were ',count,' subject lines in ',inp)    