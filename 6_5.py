# Ex 6_5: find number after '.' and convert to float
str = 'X-DSPAN-Confidence:  0.8475'
index = str.find(".")
num = str[index:]
num = float(num)
print(num)