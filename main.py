l = [1, 2, 3]

inn=ex=0

for i in l:
    new_ex = max(inn,ex)
    inn = ex + i
    ex = new_ex

print(max(inn,ex))