l = [1,2,3,[4,5,6,[7,8,[9,0]],9]]

def flat(n):
    flat_list = []
    for i in n:
        if isinstance(i,list):
            flat_list.extend(flat(i))
        else:
            flat_list.append(i)
    return flat_list

m = flat(l)
print(m)