# Given an array size of N elements, Find the count of elements which has atleast one greater element than itself!

#solution 1
l = [-3,-2,9,3,4,8,7,10,2,8,5]
high = max(l)
count = 0
for i in l:
    if i < high:
        count +=1
print(count)

#solution2

i,j = 0,1
count= 0
for i in range(len(l)):
    if i<j:
        count+=1
    else:
        j+=1
    
# Given an array of N elements, Find the count of pairs (i,j) where i+j indices such that arr[i]+arr[j]=k
l = [3,5,2,1,-3,7,8,15,6,13]
k = 10
count= 0

for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j] ==k:
            print(l[i],l[j])
            count+=1
print(count)