# Ex 10.3: function takes str and prints letters in decreasing frequency

def most_frequent(file):    
    #Read line and count letters    
    import string 
    translator = str.maketrans('','',string.punctuation) # creates translation table for .translate method
    d = dict()
    for line in file:
        line = line.lower()  #prepping line for processing
        line = line.rstrip()
        line = line.translate(translator)
        line = line.replace(' ','')
        for letter in line: #count freq of letters
            if not letter in d:
                d[letter] = 1
            else:
                d[letter] += 1

    #sort letters
    lst = list()
    for letter, count in d.items():
        lst.append((count, letter))
    lst.sort(reverse = True)
    return(lst)

#Open File
print('This program prints out the frequency of letters for any text.')
inp = input('Type in a filename for a .txt file you want to process: ')
try: fhand = open(inp)
except: 
    print("Can't find file ",inp,". File must be in same folder as this program to work.")
    quit()

output = most_frequent(fhand)
print(output)