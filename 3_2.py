# computes pay w/ overtime
inp = input("Enter Hours: ")
try: hours = float(inp)
except: 
    print("Error, please enter a numeric input")
    quit()
inp = input("Enter Rate: ")
try: rate = float(inp)
except:
    print("Error, please enter a numeric input")
    quit()
if hours > 40:
    overtime = hours - 40
    pay = (rate * 40)+(1.5*rate*overtime)
    print("Pay: ",pay)
else:
    pay = rate*hours
    print("Pay: ",pay)