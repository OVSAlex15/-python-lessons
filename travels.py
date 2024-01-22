summa1 = 0
summa1gruz = 0
summa2 = 0
summa2gruz = 0
summa3 = 0
summa3gruz = 0
l = []
file = open('travels.txt','r')
for i in file:
    s = str(i)
    parts = s.split(' ')
    print(parts)
    if int(parts[0]) == 1:
        summa1+=1
        summa1gruz +=int(parts[6])
    elif int(parts[0]) == 2:
        summa2+=1
        summa2gruz +=int(parts[6])
    else:
        summa3+=1
        summa3gruz +=int(parts[6])
l.append(summa1)
l.append(summa2)
l.append(summa3)
if int(max(l)) == 1:
    print('1 октября ',summa1gruz,' кг груза')
elif int(max(l)) == 2:
    print('2 октября ',summa2gruz,' кг груза')
else:
    print('3 октября ',summa3gruz,' кг груза')
        