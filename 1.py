x = input('input :>')
a = []
for i in range(len(x)):
    k = False
    if x[i] == '(':
        a.append(i+1)
    elif x[i] == ')' and len(a) == 0:
        print(i+1)
        k = True
        break
    else:
        a.pop()
if k == False:
    if len(a) > 0:
        print(a[0])
    else:
        print('правильная  послед')