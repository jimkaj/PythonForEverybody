# Ex 6.1: print a word in reverse
count = 0
index = -1
word = input("Type a word: ")
while count < len(word):
    print(word[index])
    index = index -1
    count = count +1
print("Done!")    