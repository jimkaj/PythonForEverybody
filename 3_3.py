#Converts numeric grade to letter grade
inp = input("Enter score: ")
try: score = float(inp)
except: 
    print("Bad Score")
    quit()
if score < 0 or score > 1:
    print("Bad Score")
    quit()
elif score >= 0 and score < .6:
    grade = "F"
elif score >= .6 and score < .7:
    grade = "D"
elif score >= .7 and score < .8:
    grade = "C"
elif score >= .8 and score < .9:
    grade = "B"
elif score >= .9 and score <= 1:
    grade = "A"
print(grade)    
    
    
    