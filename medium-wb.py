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

def binary_search()