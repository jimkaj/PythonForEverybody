# Ex 6_3: Count the number of letters in a word
def count_letter(word, letter):
    count = 0
    index = 0
    for l in word:
        if l == letter:
            count = count + 1
    return count       
InpW = input("Enter a word: ")
w = InpW.lower()
InpL = input("Enter a letter to count in the word: ")
l = InpL.lower()
print("The letter '",InpL,"' appears in ",InpW,count_letter(w, l),"times.")