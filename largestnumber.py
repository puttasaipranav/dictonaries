a = [1,2,3,4,5,6,7,36,8,9,11,3,12,32]

l,r = 0,1

while r<len(a):
    if a[l]<a[r]:
        l = r
    r+=1
print(a[l])