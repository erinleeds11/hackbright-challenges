def add_to_zero(nums):
    set_nums = set(nums)
    for num in nums:
        if -num in set_nums:
            return True

    return False
    
def concat_list(lst1, lst2):
    new_list = lst()
    new_list.extend(lst1, lst2)

def is_leap_year(year):
    """Is this year a leap year?"""

    if year % 400 == 0:
        return True

    if year % 100 == 0:
        return False

    if year % 4 == 0:
        return True

def days_in_month(date):
    imonth), year = date.split()

    if int(month) == 2

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""
    nums = list(range(1,11))
    lucky_nums = []

    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)

    return lucky_nums

def find_range(nums):
    smallest = nums[0]
    largest = nums[0]

    for num in nums:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    
    return (smallest, largest)

def has_more_vowels

def find_largest_smaller_than(nums, xnumber):
    """Find largest number in sorted list that is smaller than given number."""

    largest = int()

    for num in nums:

        if num > largest and num < xnumber:
            largest = num

def leet_speak(phrase):
    leet = {"a":@, "o":0, "e":3, "l":1, "s":5, "t":7}
    new_phrase = ''
    for letter in phrase:
        new_phrase += leet.get(letter, letter)

def snake_to_camel(phrase):
    split_phrase = phrase.split('_')
    camel = split_phrase[0]
    for i in range(1, len(split_phrase)):
        camel += split_phrase[i].title()