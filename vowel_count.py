l = 'cbaiviagvuabefcbaudverufdobdov'

def count_vowel(a):
    vowels = ['a','e','i','o','u']
    a = [i for i in a]
    data = {}
    for i in a:
        if i not in data.keys() and i in vowels:
            data[i] =1
        elif i in data.keys():
            data[i] +=1
    print(data)
count_vowel(l)