def is_palindrome(s):
   
    length = len(s)

    # Palindrome
    # s[index] == s[length-i-index]
    # For all indexes: 0 to length/2

    # Iterate up to half the length to compare corresponding characters
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False

    return True


s = "radar"
result = is_palindrome(s)
print(f"Is {s} palidrome: {result}")