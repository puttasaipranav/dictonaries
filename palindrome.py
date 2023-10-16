def check_pain(n):
    if n == n[::-1]:
        print('It is a palindrome')
    else:
        print('Not a Palindrome')

check_pain('pop')