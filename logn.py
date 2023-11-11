def inttostr(i):
    digits = '01234567'
    if i==0:
        return '0'
    result = ''
    while i>0:
        result = digits[i%10] + result
        i = i//10
    return result

a = inttostr(1230)
print(a)