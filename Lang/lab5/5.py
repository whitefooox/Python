def palindrome(s):
    s2 = s[::-1]
    if(s == s2):
        return "Палидром"
    else:
        return "Не палидром"

print(palindrome(input()))
