def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    ht = dict()

    for char in word:
        count = ht.get(char, 0) +1 

    seen_odd = False
    for value in ht.values():
        if value % 2 == 0 and seen_odd == False:
            seen_odd = True
    
    return seen_odd

print(is_anagram_of_palindrome("abbca"))