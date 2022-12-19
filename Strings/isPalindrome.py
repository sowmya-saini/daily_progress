def isPalindrome(input_str):
    length = len(input_str)
    l = length -1
    for i in range(length//2):
        if input_str[i] != input_str[l-i]:
            return "It is not palindrome"
    return "It is Palindrome"


    
print(isPalindrome("sainiinias"))
print(isPalindrome("anna"))
print(isPalindrome("civic"))
print(isPalindrome("madam"))
print(isPalindrome("easy"))
