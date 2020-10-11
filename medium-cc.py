def balanced_brackets(phrase):
    closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}

    openers = set(closers_to_openers.values())
    
    openers_seen = []

    for ch in phrase:

        if ch in openers:
            openers_seen.append(ch)
        
        elif ch in closers_to_openers:
            if openers_seen == []:
                return False
           
            if openers_seen[-1] == closers_to_openers.get(ch):
                openers_seen.pop()
            
            else:
                return False
        
        return openers_seen == []

def calculator(phrase):
    # "+ 1 2"
    list_of_items = list(reversed(phrase.split()))
    # ["2", "1", "+"]
    curr_nums = []
    total = []
    pos_operator = 0
    for ch in list_of_items:
        if ch.isdigit() == False:
            current_operator = ch
        
       
