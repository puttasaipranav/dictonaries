a = [7,1,5,6,4,3]

def buy_sell(a):
    l,r = 0,1
    maxp =0

    while r< len(a):
        if a[l] < a[r]:
            profit = a[r] - a[l]
            maxp = max(maxp,profit)
        else:
            l = r
        r+=1
    return maxp

profit = buy_sell(a)
print(profit)