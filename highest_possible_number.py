n = '123097129081'

a = [i for i in n]
a.sort(reverse=True)

highest_number = ''.join(a)
print(highest_number)