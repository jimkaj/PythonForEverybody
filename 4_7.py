#Assign letter grade using function
def computegrade(s):
    if s <= .6 and s >= 0: g = "F"
    elif s <=.7 and s > .6: g = "D"
    elif s <=.8 and s > .7: g = "C"
    elif s <=.9 and s > .8: g = "B"
    elif s <=1 and s > .9: g = "A"
    else: 
        print("Bad score")
        quit()
    return g
i = input("Enter score: ")
try:
    score = float(i)
except:
    print("Bad score")
    quit()
grade = computegrade(score)
print(grade)    
    
