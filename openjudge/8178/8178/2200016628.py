def isPalindrome(s):
    if all(s[i] == s[len(s) - 1 - i] for i in range(len(s) // 2)):
        return "yes"
    else:
        return "no"
s=input()
print(isPalindrome(s))