a = [7,1,5,6,4,3]

def max_pair(a):
    l,r = 0,1
    maxpair = 0
    pair = []
    while r < len(a):
        maxi = a[l] + a[r]
        if maxpair < maxi:
            maxpair = maxi
            pair.clear()
            pair.append(a[l])
            pair.append(a[r])
        l +=1
        r +=1
    return pair

m = max_pair(a)
print(m)