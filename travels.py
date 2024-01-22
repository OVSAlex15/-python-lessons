summa = 0
l = []
file = open('travels.txt','r')
for i in file:
    s = str(i)
    parts = s.split(' ')
    print(parts)
    if parts[0] == '1':
        summa += int(parts[4])
print(summa)

        