# Ex 8.1: write function to modify list & remove first & last element
def chop(ls):
    del ls[0]
    del ls[-1]
t = [1,2,3,4,5]
print('Before chop: ',t)
chop(t)
print('After chop: ',t)
