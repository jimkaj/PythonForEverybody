# Ex 8.2: find the bug
inp = input('Enter File Name: ')
try:
    fhand = open(inp)
    # fhand = open('mbox-short.txt')
except:
    print("Can't find file")
    quit()
count = 0 
for line in fhand:
    words = line.split()
    #print('Debug:', words)
    if len(words)==0 or words[0]!= 'From': continue
    print(words[2])
    count = count + 1
print(count)    