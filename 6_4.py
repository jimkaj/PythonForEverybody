# Ex 6.4: Use count to count how many times letter is in a word
InpW = input("Enter a word: ")
W = InpW.lower()
InpL = input("Enter a letter to find :")
L = InpL.lower()
print(InpL,"appears in",InpW,W.count(L),"times.")
