#total, count, average for series
total = 0
count = 0
average = 0
while True:
    itervar = input("Enter a number or enter 'done' ")
    if itervar == "done":
        break
    try: 
        num = float(itervar)
        total = total + num
        count = count + 1
    except:
        print("Invalid input")
        continue
print(total, count, total/count)
    