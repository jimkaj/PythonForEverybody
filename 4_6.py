# Pay program using functions
def computepay(h, r): #hours, rate
    p = h*r
    return p
def float_it(s):
    try: 
        f = float(s)
        return f
    except: 
        print("You must type a number")
        quit()
i = input("Enter Hours: ")
hours = float_it(i)   
i = input("Enter Rate: ")
rate = float_it(i)
if hours <= 40:
    pay = computepay(hours, rate)
elif hours>= 40:
    overtime = hours - 40
    pay = computepay(40, rate) + computepay(hours-40,rate*1.5)
print("Pay: ", pay)    