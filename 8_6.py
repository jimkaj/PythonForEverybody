# Ex 8.6: take list of nums until 'done' then print max/min
t = []
inp = None
while True:
    inp = input('Enter a number or type "done": ')
    if inp == 'done': break
    try: num = float(inp)
    except:
        print('You must enter a number or "done"')
        break
    t.append(num)
if len(t) == 0:
    print('No numbers were entered.')
    quit()
print('Maximum: ',max(t))
print('Minimum: ',min(t))
    
    