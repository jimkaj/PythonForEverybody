# Ex 8.4: Read Romea txt, count individual words
fhand = open('romeo.txt')
wordlist = []

# Build list of unique words
for line in fhand:
    words = line.split()
    for i in range(len(words)):
        if words[i] in wordlist: continue 
        wordlist.append(words[i])
            
#sort and print words
wordlist.sort()
print(wordlist)    