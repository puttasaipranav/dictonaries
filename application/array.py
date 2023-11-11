l = [11,13,5,6,4,3]

k,m = 0,1

j = []
for i in range(len(l)):
    if m < len(l):
        if l[m] > l[k]:
            j.append(l[m])
        k+=1
        if m != len(l):
            m+=1
    else:
        j.append(l[m-1])
print(j)