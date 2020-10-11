class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: get index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        #does not matter it is forever loop cuz already checked index
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx +=1
    
    def erase(self, index):
        if index >= self.length():
            print("ERROR: erase index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node  = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                #erases current node
                return
            cur_idx += 1
        

        

# my_list = LinkedList()
# my_list.display()
# brownie = Node("yum")
# my_list.append(1)
# my_list.display()
