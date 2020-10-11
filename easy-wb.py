def add_to_zero(nums):
    """Given list of ints, return True if any two nums sum to 0."""
    
    set_nums = set(nums)

    for num in nums:
        if -num in set_nums:
            return True


def concat_lists(lst1, lst2):
    """ Combine lists"""

    for item in lst1:
        lst2.append(item)

def days_in_month(date):
    """How many days are there in a month?"""

    month, year = date.split()

    if month == 2

    

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    nums = list(range(1, 11))
    unique_nums = list()

    for i in range(len(n)):
        unique = random.choice(nums)
        unique_nums.append(unique)
        nums.remove(unique)

    return unique_nums


   

def find_range(lst):
   


def has_more_vowels(strng):
   
def is_prime(num):
    """Is a number a prime number?"""

    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def is_palindrome(word):
    """Return True/False if this word is a palindrome."""
     for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False

    return True
    

def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

def translate_leet(phrase):
    """Translates input into "leet-speak"."""

    leet = {"a": "@", "o":0, "e": 3, "l": 1, "s":5, "t": 7}
    leet_phrase = []

    for char in phrase.lower():
        if char in leet.keys():
            leet_prase.append(leet[char])
        leet_phrase.append(char)

    return "".join(leet_phrase)

def find_longest_word(words):
    """Return longest word in list of words."""
    longest = words[0]
    for word in words:
        if word > longest:
            longest = word
    
    return len(longest)
    # good info on whiteboarding HB


def is_pangram(sentence): #STAR
    """Given a string, return True if it is a pangram, False otherwise."""

    alphabet = [a, b, c, d, ,,e, ...]
    set_phrase = set(sentence).
    list_phrase = list(set_phrase)

    for char in list_phrase.lower():
        if char in alphabet:
            alphabet.remove(char)
    
    if len(alphabet) == 0:
        return True
    
    return False


def pig_latin(phrase):
    """Turn a phrase into pig latin.

    There will be no uppercase letters or punctuation in the phrase.

        >>> pig_latin('hello awesome programmer')
        'ellohay awesomeyay rogrammerpay'
    """

    for word.lower() in phrase:
        first_letter = word[-1]
        word.remove(first_letter)
        word[-1] = f"{first_letter}ay"




    
    




    








