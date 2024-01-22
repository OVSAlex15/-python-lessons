summa = 0
l = []
file = open('travels.txt','r')
for i in file:
    s = str(i)
    parts = s.split(' ')
    print(parts)
    if parts[2] == 'Липки':
        summa += int(parts[6])
print(summa)

        