#step 1
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Step 2
class LinkedList:
    def __init__(self):
        self.head = None

#Step 3
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

#step 4
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display() 

#step 5
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)
ll.display()  

#Step 6
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)
ll.display() 
ll.delete(2)
ll.display()  

#Step 7
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)
ll.display() 
ll.delete(2)
ll.display()  
print(ll.search(4))  
print(ll.search(5))  

#Step 7
class LinkedList:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.insert(4, 1)
ll.display() 
ll.delete(2)
ll.display()
ll.reverse()
ll.display()  

#Exercise 1
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
head = ListNode(8, ListNode(5, ListNode(6, ListNode(7, ListNode(4)))))
middle = find_middle(head)
print(middle.value) 

#Exercise 2
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          
        fast = fast.next.next     

        if slow == fast:
            return True           

    return False   
node1 = ListNode(3)
node2 = ListNode(2)
node1.next = node2
print(has_cycle(node1))  
             
#Exercise 3
class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next = next_node

def remove_duplicates(head):
    if head is None:
        return None

    seen = set()  
    current = head
    seen.add(current.value)  

    while current.next:  
        if current.next.value in seen:  
            current.next = current.next.next  
        else:
            seen.add(current.next.value)  
            current = current.next  

    return head  

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

print("Original linked list:")
print_linked_list(head)
remove_duplicates(head)
print("Linked list after removing duplicates:")
print_linked_list(head)

#Exercise 4
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def merge_two_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    return dummy.next
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
def print_linked_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")
list1 = create_linked_list([0,2,4])
list2 = create_linked_list([1,3,5])
merged_list = merge_two_sorted_lists(list1, list2)
print_linked_list(merged_list)
