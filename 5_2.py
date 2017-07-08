#total, count, average for series
total = 0
count = 0
min = None
max = None
while True:
    itervar = input("Enter a number or enter 'done' ")
    if itervar == "done":
        break
    try: 
        num = float(itervar)
    except:
        print("Invalid input")
        continue
    total = total + num
    count = count + 1
    if max is None or num > max:
        max = num
    if min is None or num < min:
        min = num
print(total, count, max, min)
    