n = 10

def f(n):
    a = []
    for i in range(n):
        if len(a) == 0:
            a.append(i)
            a.append(i+1)
        else:
            a.append(a[-2]+a[-1])
    print(a)

f(n)