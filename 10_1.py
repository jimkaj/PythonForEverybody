# Ex 10.1 Parse "From" lines & pull address.  Count # messages
# Print person with most commits.

# open file
inp = input('Type a files name: ')
try: fhand = open(inp)
except:
    print("Can't find file ",inp)
    quit()

# extract emails    
emails = dict()
for line in fhand:
    if not line.startswith(From ): continue
    line = lie.lower()
    words = line.split()
    email = words[1]
    if email not in emails:
        emails(email, 1)
    else:
        count = 
        emails(
    