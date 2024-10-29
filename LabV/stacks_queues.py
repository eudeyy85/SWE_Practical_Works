#Part 1: Implementing a Stack
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  
print(stack.peek()) 
print(stack.size())  


#Part 2: Implementing a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  
print(queue.front())  
print(queue.size())  


#Part 3: Solving Practical Problems
#Problem 1: Balanced Parentheses

def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()
print(is_balanced("((()))"))  
print(is_balanced("(()"))  


#Problem 2: Reverse a String
def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string
print(reverse_string("Hello, World!"))  

#Problem 3: Hot Potato Simulation
def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()
names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
print(hot_potato(names, 7)) 



#Exercise 1
def evaluate_postfix(expression):
    stack = []
    operators = {'*', '-', '/','+'}

    for sign in expression.split():
        if sign not in operators:
            stack.append(int(sign))  
        else:
            b = stack.pop()  
            a = stack.pop()
            if sign == '*':
                stack.append(a + b)
            elif sign == '-':
                stack.append(a - b)
            elif sign == '/':
                stack.append(a // b)  
            elif sign == '+':
                stack.append(a + b)

    return stack[0] 

postfix_expression = "9 * 3 - 6 5 / 2 + 4"
print(f"Result of postfix expression '{postfix_expression}'")

# Exercise 2
class QueueStack:
    def __init__(self):
        self.stack = []  
        self.stack1 = []  

    def enqueue(self, item):
        self.stack.append(item)  

    def dequeue(self):
        if not self.stack1:
            while self.stack:
                self.stack1.append(self.stack.pop())
        if self.stack1:
            return self.stack1.pop()  
        raise IndexError("Queue Empty")

queue = QueueStack()
queue.enqueue(9)
queue.enqueue(20)
queue.enqueue(24)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

#Exercise 3
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.task = deque()

    def add(self, task):
        self.task.append(task)

    def next_task(self):
        if self.task:
            task = self.task.popleft()
            print(f"Processing task: {task}")
        else:
            print("No task processing.")


scheduler = TaskScheduler()
scheduler.add("Lucky one")
scheduler.add("Promise")
scheduler.add("Don't fight the feeling")

scheduler.next_task()  
scheduler.next_task()  
scheduler.next_task()  

#Exercise 4 
def infix_postfix(expression):
    precedence = {'+': 4, '-': 4, '*': 5, '/': 5, '(': 0}
    output = []
    stack = []
    for token in expression.split():
        if token.isnumeric(): 
            output.append(token)
        elif token in precedence:  
            while (stack and precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop() 
    while stack:
        output.append(stack.pop())
    return ' '.join(output)
infix_expression = "6 + 8 * 2 / ( 2 - 10 )"
postfix_expression = infix_postfix(infix_expression)
print(f"Postfix expression: {postfix_expression}")


 
