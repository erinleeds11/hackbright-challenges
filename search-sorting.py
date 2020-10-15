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

    def get_hash(key):
        h = 0
        for char in key:
            h += ord(char)
        return h % 100