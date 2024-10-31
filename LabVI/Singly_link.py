class element:
    def __init__(self, value):
        self.value = value
        self.next = None

class list:
    def __init__(self):
        self.head = None

    def append(self, value):
        if not self.head:
            self.head = element(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = element(value)

    def middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.value if slow else None
    
linked_list = list()
linked_list.append(5)
linked_list.append(7)
linked_list.append(1)
linked_list.append(9)
linked_list.append(4)

middle_value = linked_list.middle()
print("Middle element is:", middle_value) 


