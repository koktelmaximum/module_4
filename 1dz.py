def is_palindrome(s):
    reversed_s = s[::-1]
    if s == reversed_s:
        return True
    else:
        return False
s= input('введите слово')

print(is_palindrome(s))