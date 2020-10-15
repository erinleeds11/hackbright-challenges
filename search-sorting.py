#Binary search simple

def binary_search(sequence, item):
    start_idx = 0 
    last_idx = len(sequence) - 1
    found = False

    while begin_index <= end_index:
        midpoint = start_idx + (last_idx - start_idx) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            found =  True
        elif item < midpoint:
            last_idx = midpoint -1
        elif item > midpoint:
            start_idx = midpoint + 1

    return found

    #Simple hash function

    class HashTable:
        def __init__(self):
            self.max = 100
            self.lst = [None for i in range(self.max)]
        
        def get_hash(self, key):
            h = 0
            for char in key:
                h += ord(char)
            return h % self.max
            
        def add(self, key, value):
            h = self.get_hash(key)
            self.lst[h] = value
        
        def get(self, key):
            h = self.get_hash(key)
            return self.lst[h] 