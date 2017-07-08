# Ex 7.1: Print lines of text in caps
inp = input("Enter a file name: ") # use mbox-short.txt
try:
    fhand = open(inp)
except:
    print("Could not find file.")
    quit()
for line in fhand:
    line = line.upper()
    print(line)

