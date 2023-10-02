words = ['cat','dog','small','big','fat']
note1 = 'cayt'
note2 = 'goatd'
note3 = 'mals'
note4 = 'fnlkdsbc'
note5 = 'cjhdvcjbascu'

def check(words,note):
    a = {i:note.count(i) for i in note}
    
    for i in words:
        c = {j:i.count(j) for j in i}
        result = all(key in a for key in c) and all(c[key] <= a[key] for key in c)
        return [result,i]
            
a= check(words,note1)
if a[0]:
    print(a[1])
else:
    print('-')
