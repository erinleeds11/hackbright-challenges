def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    ht = dict()

    for char in word:
        count = ht.get(char, 0) +1 
        ht[char] = count

    seen_odd = False
    for value in ht.values():
        if value % 2 == 0 and seen_odd == False:
            seen_odd = True
    
    return seen_odd

print(is_anagram_of_palindrome("abbca"))

def balanced_parens(phrase):

    parens = 0

    for char in phrase:
        if char == "(":
            parens+=1
        elif char == ")":
            parens -=1
        elif parens == -1:
            return False
    return parens == 0

def decode(phrase):

    i = 0
    decoded = ''
    while i < len(s):
        num_to skip = phrase[i] + 1
        decoded += phrase[num_to_skip]

        i+=1

    return decoded

def fit_str_to_width():

    tokens = list(reversed(string.split))
    curr_line = []
    total_lines = []

    while tokens:
        word = tokens[-1]
        if len(' '.join(curr_line + [word])) <= limit:
            curr_line.append(tokens.pop())
        
        else:
            if curr_line:
                total_lines.append(' '.join(curr_line))
                
            curr_line = []
    
    total_lines.append(' '.join(curr_line))

    for line in total_lines:
        print(line)


def balenced_parens(s):
    parens = 0
    chs = set(["(", ")"])
    for ch in s:
        if ch in chs:
            if ch == "(":
                parens +=1
            elif ch == ")" and parens >= 1:
                parents -=1
    return parens == 0

def binary_search(val):
    """Using binary search, find val in range 1-100. Return # of guesses."""

    assert 0 < val < 101, "Val must be between 1-100"

    num_guesses = 0

    higher_than  = 0
    lower_than = 101
    guess = None

    while guess != val:
        num_guesses += 1
        guess = (lower_than - higher_than) // 2 + higher_than

        if val > guess:
            higher_than = guess

        elif val < guess:
            lower_than = guess



    return num_guesses

def count_recursively(lst):
    """Return number of items in a list, using recursion."""

     if not lst:
        return 0

    return 1 + count_recursively(lst[1:])