

def compress_string(word):

    count = 0
    new_string = [] 
    prev = '' 
    for char in word:
        if char != prev:
            new_string.append(prev)
            if count > 1:
                new_string.append(str(int(count)))
            prev = char 
            count =0
        
        count +=1

def decode(word):

    new_list = []
    current_idx = 0
    rel_letter = ''
    while current_idx < len(word):

        num_to_skip = int(word[current_idx])
        current_idx += num_to_skip + 1

        new_list.append(word[current_idx])

        current_idx +=1
    
    return "".join(new_list)
        
def fit_to_width(phrase, limit):

    tokens = list(reversed(phrase)) # do this so you can pop
    lines = [] 
    curr_line = []


    while tokens:
        word = tokens[-1]
        if len(' '.join(curr_line + [word])) <= limit:
            curr_line.append(tokens.pop(0))
        
        else:
            if curr_line:
                lines.append(' '.join(curr_line))
            curr_line= [] 
    
    for line in lines:
        print(line)



def missing_num(nums, max):
    num_set = set(list(range(1, max+1)))
    #set(1, 2, 3, 4, 5, 6 7, 8, 9, 10)

    for num in nums:
        num_set.remove(num)
    
    return num_set


compress(phrase)

prev = ""
count = 0
new_phrase = []



def pangram(phrase):

    letters = set()
    phrase = replace(" ", "")
    for char.lower() in phrase:
        if char.isalpha():
            letters.add(char)
    
    return len(letters) == 26

def pig_latin(phrase):

    list_words = phrase.split()
    vowels = {a, e, i, o, u}
    pig_phrase = []
    for word in list_words:
        if word[0] in vowels:
            pig_word = word[1:]+ 'yay'
        else:
            pig_word = word[1:]+word[0] + 'ay'
        pig_phrase.append(pig_word)
    
    return " ".join(pig_phrase)


def deduped(nums):
    if nums == []:
        return nums
    
    seen = {}
    new = []
    for num in nums:
        if num not in seen:
            new.append()
            seen.add(num)

def show_even_nums(nums):

    return [i for i, num in enumerate(nums) if num%2==0]
def split(astring, splitter):
    """Split a string by splitter and return list of splits."""

    new_list = []
    for char in astring:
        phrase = ""
        if char != splitter:
            phrase += char
        else:
            new_list.append(phrase)
            phrase = ""

def truncate_repeats(phrase):
    new_phrase = []
    prev = ''

    for ch in phrase:
        if ch != prev:
            new_phrase.append(ch)
            prev = ch

    return "".join(new_phrase)



    for i in range(len(phrase)):
        if current 


   def an_of_pal(phrase):

       ht = {}
       for ch in phrase:
           count = ht.get(char, 0) + 1
           ht[ch] = count

        seen_odd = False
        for key, value in ht.items():
            if value % 2 !== 0:
                if seen_odd == False:
                    seen_odd == True
                else:
                    return False
        return True

    def compress_string(phrase):

        compressed = ""
        prev = ''
        count = 0
        for ch in phrase:
            if ch != prev:
                compressed += prev
                if count > 1:
                    compressed += count
                    count = 0
                    prev = c
            
            count +=1
            prev = ch
    
    def decode_string(phrase):
        decoded =''
        i = 0
        while i < len(phrase):
            num_to_skip = phrase[i] + 1
            decoded += phrase[num_to_skip]
            i += num_to_skip



def missing_numer(nums):
    set_nums = set(list(range(1, nums+1))

    for num in nums:
        if num in set_nums:
            set_nums.remove(num)
    
    return set_nums.pop()

def pangram(phrase):

    return len{ch.lower() for ch in phrase.split() if word.isalpha()} == 26

def show_evens(nums):

    return [num for index, num in enumerate(nums) if num % 2==0]

def split_str{()}
