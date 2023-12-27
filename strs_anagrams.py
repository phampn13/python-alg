def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Anagram
    # Same length
    # If sort the characters, the two sorted must be equal
    return sorted(str1) == sorted(str2)

word1 = "Listen"
word2 = "Silent"
result = are_anagrams(word1, word2)

print(result)