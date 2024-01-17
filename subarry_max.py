l = [-20,10,-12,6,5,-3,8,9]
b = []
# kadaen's algo
sum = 0
for i in l:
    sum += i
    b.append(i)
    if sum <0:
        sum =0
        b.clear()
print(sum,b)