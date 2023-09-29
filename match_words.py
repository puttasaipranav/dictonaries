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
        result = all(key in a for key in c)
        if result:
            res = all(c[key] <= a[key] for key in c)
            if res:
                return i
            else:
                print('-')
            
check(words,note3)
