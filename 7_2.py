# Ex 7.2 Look for "X-DSPAM-Confidence: .8473" and average numbers
inp = input("Enter a file name: ") # use mbox.txt & mbox-short.txt
try: fhand = open(inp)
except:
    print("Could not find file ",inp)
    quit()
sum = 0
count = 0
for line in fhand:
    if line.find('X-DSPAM-Confidence') != -1:
        start = line.find('X-DSPAM-Confidence:') + 20
        num = line[start:]
        num = float(num)
        sum = sum + num
        count = count + 1
print('Average span confidence: ', (sum/count))    
        