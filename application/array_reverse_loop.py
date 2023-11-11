l = [11,13,2,5,3,4]
n = len(l)

max = l[-1]
leaders = [l[-1]]

for i in range(n-2,-1,-1):
    if max< l[i]:
        max = l[i]
        leaders.append(l[i])
print(leaders[::-1])