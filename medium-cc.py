def balanced_brackets(phrase):
    closers_to_openers = {")": "(", "]": "[", "}": "{", ">": "<"}
    openers = set(closers_to_openers.values())
    openers_seen = []

    for ch in phrase:
        if ch in openers:
            openers_seen.append(ch)
        elif ch in closers_to_openers:
            if openers_seen ==[]:
                return False
            elif openers_seen[-1] = closers_to_openers[ch]:
                openers_seen.pop()
            else:
                return False
    
    return openers_seen == []
        
       
#BST ADD CHILD

class Node(object):
    '''Basic Node class'''

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def insert(self, new_data):

        if new_data >= self.data:
            if self.right is None:
                self.right = Node(new_data)
            else:
                self.right.insert(new_data)
        else:
            if self.left is None:
                self.left = Node(new_data)
            else:
                self.left.insert(new_data)


#VALIDATE BST

class Node(object):
    '''Basic Node class'''

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

class Solution(object):
    def isValid(self, root):
    
    def helper(self, root, minValue, maxValue):
        if root is None:
            return True
        
        if root.data <= minValue or root.data >= maxValue:
            return False
        validateLeft = helper(self, root.left, minValue, root.data)
        validateRight = helper(self, root.right, root.data, max_value)
        return validateLeft == validateRight

#Polish Notation Calc

def calc(s):
    tokens = s.split()
    operand2 = int(s.pop())
    while tokens:
        operand1 = int(s.pop())
        operator = s.pop()
        if operator == '*':
            operand2 *=operand1
        elif operator == '+':
             operand2 +=operand1
        elif operator == '-':
             operand2 -=operand1
        elif operator == '/':
             operand2 //=operand1
        return operand2