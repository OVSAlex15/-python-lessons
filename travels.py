l=[]
d = {}
file = open('travels.txt','r')
for i in file:
    s = str(i)
    parts = s.split(' ')
    if parts[2] in d:
        d[parts[2]] += int(parts[6])
    else:
        d[str(parts[2])]=int(parts[6])
    
keys_list = list(d.keys())
print(len(keys_list))
print(d)
       

         
        

    

        