# SWE_Practical_Works

# What I Implemented In Practical 2

# Exercise 1 [Modify the program to count the number of unique words in the text.]
While doing this exercise I implemented funtion that splits the input text(sample.txt) into list of individual words and spacing it.Next created a set  the list of words that contain the unique elements and remove the duplicates word and then used the function [len(unique_words)] to calculates the number of elements in the set, which is the count of unique words.

# Exercise 2 [Add a function to find the longest word in the text.]
While doing this exercise I implemented funtion that splits the input text(sample.txt) similar to exercise 1, used the [max(words, key=len)] to find the maximun element in the list of words and the key=len function specifies that the maximum element should be determined based on the length of each word.

# Exercise 3 [Implement a feature to count the occurrences of a specific word (case-insensitive).]
While doing this exercise I implemented function to split input text like in above exercises,used the function [words.count(word.lower())] to count() method of the list object to efficiently count the number of occurrences of the word'The/the' within the words list and the word would be treated as same word.

# Exercise 4 [Create a function to calculate the percentage of words that are longer than the average word length.]
While doing this exercise I implemented function [sum(len(word)] for word in words to calculate the total length of all the words, used [average_length = total_length / len(words)] calculates the average word length by dividing the total length by the number of words. Even used [longer_words_count = sum(1 for word in words if len(word) > average_length)] counts the number of words longer than the average length using a generator expression. Moreover, used the function [percentage = (longer_words_count / len(words)) * 100] to calculate the percentage of longestp ppppppppppwords by dividing the count of long words by the total number of words and multiplying by 100.



# What I Implemented In Practical 3

# Exercise 1 [Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.]
In this exercise I implemented the function to generate Fibonacci sequences from 20 to 25 upto specified length.It starts a list with the first two terms and alliteratively calculates the next term by adding the previous two terms and then it returns the funtion to the the first n terms of the sequence.

# Exercise 2 [Implement a function that finds the index of the first Fibonacci number that exceeds a given value.]
In this exercise I implemented funtion to calculate the index of the first Fibonacci number that go beyound the given value. It alliteratively claculates the next number which starts with 10th and 11th fibonacci number(5 & 10) and the function returns the index when the calculated fibonacci number exceeds thegiven value.

# Exercise 3 [Create a function that determines if a given number is a Fibonacci number.]
In this exercise I implemented the function to determine whether a given number is a Fibonacci number.Used the function that a number n is a Fibonacci number if and only if either 5n^2+4 or 5n^2-4 is a perfect square and then calculates the values and checks if they are perfect squares using a helper function is_perfect_square.

# Exercise 4 [Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.]
In this exercise I implemented the function to calculates the ratio of consecutive fibonacci numbers upto n term,it starts a list with the first 1 fibonacci numbers(0 & 2) and alliteratively calculates the next terms,then calculates the ratios of consecutive terms and stores them in a list.Lastly, it prints out the calculated ratios with the index of the Fibonacci numbers.

# Discussion Questions
Q1.What are the advantages and disadvantages of the recursive approach compared to the iterative approach?

Ans: 
1.Recusive Approach:
  Advantages:
     1.Simplicity and Readability: it is more direct and easier to understand.

     2.Functional Programming: Recursive functions are a fundamental concept in functional programming, where they are used to define functions that operate on data structures in a declarative style.

     3.Natural Representation of Certain Problems:they break down the problem into subproblems of the same type and has straightforward and direct implementation of these problems.

  Disadvantages:
     1.Memory Usage: high memory usage as it uses the call stack to manage function calls which can lead to overflow errors if its too deep.

     2. Stack Overflow: Deep recursion can lead to stack overflow errors if the function call stack exceeds the available memory.

2.Iterative Approach
  Advantages:
     1.Efficiency in Memory and Performance: it use less memory than recursive solutions as they don’t add extra frames to the call stack.
     
     2.Better for Large Inputs:For problems that involve large inputs or require deep recursive calls, iteration is often the only feasible option, as it won’t lead to stack overflow errors.

  Disadvantages:
     1.More Code in Some Cases: it can sometimes require additional code to simulate recursion.

     2.Readability: it can be less readable and more complex for problems that are naturally expressed recursively.


Q2.How does memoization improve the performance of the recursive function? Are there any drawbacks?

Ans:
Memoization is a technique used to improve the performance of recursive functions by storing the results of function calls and reusing them when the same input is encountered again.

Drawbacks of Memoization:

1.Increased Memory Usage: it requires additional memory to store previously computed results.

2.Cache Management: depending on the programming language or memoization, the cache might not automatically clear itself, potentially causing memory issues.


Q3.In what scenarios might you prefer to use a generator function over other implementations?

ANS:- When working with large datasets that cannot fit into memory as a generator function allows you to process each item individually, reducing memory usage and simplifying code for complex iterations as it simplify code that requires complex or conditional iteration.

Q4.How does the space complexity differ between these implementations?

Ans:- 
The space complexity differs significantly between implementations, especially when comparing generators, lists and other data structures that store all results, recursive functions, and iterative functions as:

1.Generator Functions:  the space complexity remains constant regardless of the sequence length, as items are not stored in memory after being yielded.

2.Lists and Other Data Structures that Store All Results: it store every item in memory simultaneously and it is less efficient for large data sets.

3.Recursive Functions: recursive call adds a new frame to the call stack, and the stack’s size is directly proportional to the depth of the recursion which can lead to stack overflow for deep recursions if the call stack exceeds the system’s memory limit.

4.Iterative Implementations: that don’t store intermediate results or large data structures use constant space and they that don’t store intermediate results or large data structures use constant space.



# What I Implemented In Practical 4

# Exercise 1 [Modify the linear search function to return all indices where the target appears, not just the first one.] 
While doing this exercise I implemented the function that is to designed to find all indices of the target value within the array. Used the function [linear_search_all] to make an list of elements[arr] and target tha value we are searching for [target],used function [indices] to store the indices of the target value found in [arr] and used the for loop repeats over each element in [arr] using index[i].Then use the condition to check if the current element in index[i] is equal to the target value and if match is found, the current index [i] is appended to the indices list. Lastly, the function  returns the indices list, which contains the indices of the of all the target values in the [arr].


# Exercise 2 [Implement a function that uses binary search to find the insertion point for a target value in a sorted list.]
While doing this exercise I implemented the function to set the start and end of the list, used the function loop to continue till the left is less or equal to right, the mid funtion calculates the average of left and right and returns if the mid funtion is equal to the target the function returns mid, if the mid funtion is less than the target the left pointer is moved to mid + 1 to search the right half and if the mid funtion is greater than the right pointer is moved to mid -1 to search the left half.

# Exercise 3[Create a function that counts the number of comparisons made in each search algorithm.]
While doing this exercise I implemented the function to initialize the comparison count to 2 and loop through each element in the array and also increment the comparison count by 4 to check each element then check if the current element is target, if it is,return the index and count the number of comparisons. In addition, if it is not, return -2 and the count the comparison.Next the function will check each element in[arr].

# Exercise 4 [Implement a jump search algorithm and compare its performance with linear and binary search.]
While doing this exercise I implemented the function that initialized beginning and end of the array and used while loop so that it runs as long as left is less or equal to the right.Followed by the function to calculate the mid element of the current search in the array then applied the function to check if mid element is equa, less or greater to the target so that the function can indicate the target is found,target must be in the right half of array or the target must be in the left half of array then if loop does not find the target the function returns -1.



# What I Implemented In Practical 5

# Exercise 1 [Implement a function that uses a stack to evaluate postfix expressions.]
While doing this exercise I implemented the function that starts a list (stack) to hold numbers during evaluting process and set an opretors [*,-,+,/,=]. Used the split funciton to split into sign(numbers & opretors) and if the token is not an operator it is converted to an integer and pushed onto the stack, if the token is an operator, the function Pops the top two numbers from the stack (b and a).

# Exercise 2 [Create a function that uses two stacks to implement a queue.]
While doing this exercise I implemented the function that that call enqueue(item) where the item is simply pushed onto self.stack and if self.stack1 is empty, it transfers all elements from self.stack to self.stack1 in reverse then it pops the top element.

# Exercise 3 [Use a queue to implement a basic task scheduler that processes tasks in the order they were added.]
While doing this exercise I implemented the function that  allows us to efficiently append and pop items from both ends with the [import deque from the collections].Created an empty deque called [self.task] to hold the tasks,used the function to takes a task as an argument and adds it to the end of the deque using the append method which allows us to keep track of tasks in the order they were added. Added the methob to check if there are any task in the deque. The  tasks [if self.task:], it removes and retrieves the first task from the front of the deque using popleft(), It then prints a message indicating which task is being processed and then if there are no tasks, it prints "No task processing."



# Exercise 4 [Implement a function that uses a stack to convert infix expressions to postfix.]
I implemented the function where precedence dictionary defines the precedence of operators (Higher numbers indicate higher precedence), the function the output list will hold the resulting postfix expression and the stack is used to temporarily hold operators and parentheses. The function operands directly append to the output, an operator at the top of the stack with greater or equal precedence, pop from the stack to output and push the current operator onto the stack. The function [left parenthesis & right parenthesis] is used to push onto the stack & pop from the stack to output until a left parenthesis is encountered respectively.

# What I Implemented In Practical 5

# Exercise 1 [Implement a method to find the middle element of the linked list.]
I created the class grounp(node) to represent each individual item in the linked list where the list stores the attributes of the (value) to store data for the node and the (next) points to the next node in the list but I used none so it doesn't link to any other node yet. Made the (list) class to manage the entire linked list and added element to the list using append method which adds a new node to the end of the list. Finally, the find_method finds the middle element of the linked list.