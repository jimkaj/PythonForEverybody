# Ex 8.1b: Function takes list and returns new list of middle only
def middle(ls):
    x = ls[1:-1]
    return x
t = [1,2,3,4,5]
print('Before middle: ',t)
New = middle(t)
print('After middle: ',New)
print('Original list: ',t)    