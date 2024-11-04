# SWE_Practical_Works

# What I Implemented In Practical 2

## Exercise 1 [Modify the program to count the number of unique words in the text.]
While doing this exercise I implemented funtion that splits the input text(sample.txt) into list of individual words and spacing it.Next created a set  the list of words that contain the unique elements and remove the duplicates word and then used the function [len(unique_words)] to calculates the number of elements in the set, which is the count of unique words.

## Exercise 2 [Add a function to find the longest word in the text.]
While doing this exercise I implemented funtion that splits the input text(sample.txt) similar to exercise 1, used the [max(words, key=len)] to find the maximun element in the list of words and the key=len function specifies that the maximum element should be determined based on the length of each word.

## Exercise 3 [Implement a feature to count the occurrences of a specific word (case-insensitive).]
While doing this exercise I implemented function to split input text like in above exercises,used the function [words.count(word.lower())] to count() method of the list object to efficiently count the number of occurrences of the word'The/the' within the words list and the word would be treated as same word.

## Exercise 4 [Create a function to calculate the percentage of words that are longer than the average word length.]
While doing this exercise I implemented function [sum(len(word)] for word in words to calculate the total length of all the words, used [average_length = total_length / len(words)] calculates the average word length by dividing the total length by the number of words. Even used [longer_words_count = sum(1 for word in words if len(word) > average_length)] counts the number of words longer than the average length using a generator expression. Moreover, used the function [percentage = (longer_words_count / len(words)) * 100] to calculate the percentage of longestp ppppppppppwords by dividing the count of long words by the total number of words and multiplying by 100.


# What I Implemented In Practical 3

## Exercise 1 [Modify the iterative function to return a list of Fibonacci numbers up to n, instead of just the nth number.]
In this exercise I implemented the function to generate Fibonacci sequences from 20 to 25 upto specified length.It starts a list with the first two terms and alliteratively calculates the next term by adding the previous two terms and then it returns the funtion to the the first n terms of the sequence.

## Exercise 2 [Implement a function that finds the index of the first Fibonacci number that exceeds a given value.]
In this exercise I implemented funtion to calculate the index of the first Fibonacci number that go beyound the given value. It alliteratively claculates the next number which starts with 10th and 11th fibonacci number(5 & 10) and the function returns the index when the calculated fibonacci number exceeds thegiven value.

## Exercise 3 [Create a function that determines if a given number is a Fibonacci number.]
In this exercise I implemented the function to determine whether a given number is a Fibonacci number.Used the function that a number n is a Fibonacci number if and only if either 5n^2+4 or 5n^2-4 is a perfect square and then calculates the values and checks if they are perfect squares using a helper function is_perfect_square.

## Exercise 4 [Implement a function that calculates the ratio between consecutive Fibonacci numbers and observe how it approaches the golden ratio.]
In this exercise I implemented the function to calculates the ratio of consecutive fibonacci numbers upto n term,it starts a list with the first 1 fibonacci numbers(0 & 2) and alliteratively calculates the next terms,then calculates the ratios of consecutive terms and stores them in a list.Lastly, it prints out the calculated ratios with the index of the Fibonacci numbers.

## Discussion Questions
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

## Exercise 1 [Modify the linear search function to return all indices where the target appears, not just the first one.] 
While doing this exercise I implemented the function that is to designed to find all indices of the target value within the array. Used the function [linear_search_all] to make an list of elements[arr] and target tha value we are searching for [target],used function [indices] to store the indices of the target value found in [arr] and used the for loop repeats over each element in [arr] using index[i].Then use the condition to check if the current element in index[i] is equal to the target value and if match is found, the current index [i] is appended to the indices list. Lastly, the function  returns the indices list, which contains the indices of the of all the target values in the [arr].

## Exercise 2 [Implement a function that uses binary search to find the insertion point for a target value in a sorted list.]
While doing this exercise I implemented the function to set the start and end of the list, used the function loop to continue till the left is less or equal to right, the mid funtion calculates the average of left and right and returns if the mid funtion is equal to the target the function returns mid, if the mid funtion is less than the target the left pointer is moved to mid + 1 to search the right half and if the mid funtion is greater than the right pointer is moved to mid -1 to search the left half.

## Exercise 3[Create a function that counts the number of comparisons made in each search algorithm.]
While doing this exercise I implemented the function to initialize the comparison count to 2 and loop through each element in the array and also increment the comparison count by 4 to check each element then check if the current element is target, if it is,return the index and count the number of comparisons. In addition, if it is not, return -2 and the count the comparison.Next the function will check each element in[arr].

## Exercise 4 [Implement a jump search algorithm and compare its performance with linear and binary search.]
While doing this exercise I implemented the function that initialized beginning and end of the array and used while loop so that it runs as long as left is less or equal to the right.Followed by the function to calculate the mid element of the current search in the array then applied the function to check if mid element is equa, less or greater to the target so that the function can indicate the target is found,target must be in the right half of array or the target must be in the left half of array then if loop does not find the target the function returns -1.


# What I Implemented In Practical 5

## Exercise 1 [Implement a function that uses a stack to evaluate postfix expressions.]
While doing this exercise I implemented the function that starts a list (stack) to hold numbers during evaluting process and set an opretors [*,-,+,/,=]. Used the split funciton to split into sign(numbers & opretors) and if the token is not an operator it is converted to an integer and pushed onto the stack, if the token is an operator, the function Pops the top two numbers from the stack (b and a).

## Exercise 2 [Create a function that uses two stacks to implement a queue.]
While doing this exercise I implemented the function that that call enqueue(item) where the item is simply pushed onto self.stack and if self.stack1 is empty, it transfers all elements from self.stack to self.stack1 in reverse then it pops the top element.

## Exercise 3 [Use a queue to implement a basic task scheduler that processes tasks in the order they were added.]
While doing this exercise I implemented the function that  allows us to efficiently append and pop items from both ends with the [import deque from the collections].Created an empty deque called [self.task] to hold the tasks,used the function to takes a task as an argument and adds it to the end of the deque using the append method which allows us to keep track of tasks in the order they were added. Added the methob to check if there are any task in the deque. The  tasks [if self.task:], it removes and retrieves the first task from the front of the deque using popleft(), It then prints a message indicating which task is being processed and then if there are no tasks, it prints "No task processing."

## Exercise 4 [Implement a function that uses a stack to convert infix expressions to postfix.]
I implemented the function where precedence dictionary defines the precedence of operators (Higher numbers indicate higher precedence), the function the output list will hold the resulting postfix expression and the stack is used to temporarily hold operators and parentheses. The function operands directly append to the output, an operator at the top of the stack with greater or equal precedence, pop from the stack to output and push the current operator onto the stack. The function [left parenthesis & right parenthesis] is used to push onto the stack & pop from the stack to output until a left parenthesis is encountered respectively.


# What I Implemented In Practical 5

## Exercise 1 [Implement a method to find the middle element of the linked list.]
I created the class grounp(node) to represent each individual item in the linked list where the list stores the attributes of the (value) to store data for the node and the (next) points to the next node in the list but I used none so it doesn't link to any other node yet. Made the (list) class to manage the entire linked list and added element to the list using append method which adds a new node to the end of the list. Finally, the find_method finds the middle element of the linked list.

## Exercise 2 [Create a method to detect if the linked list has a cycle.]
Implement a  method checks for a cycle in the linked list, the slow pointer moves one node at a time, the fast pointer moves two nodes at a time and if a cycle exists, slow and fast will eventually meet inside the cycle, if fast reaches the end (None), the list has no cycle.  Create an instance of linkedlist called linked_list, append values to link_list and checks if there’s a cycle with has_cycle(), it should return False. Then, manually create a cycle by setting the next of the last node (5) to point to the node with value 3 and also check again with has_cycle(), and it should return True.

## Exercise 3 [Implement a method to remove duplicates from an unsorted linked list.]
Implemented the method appends a new node with the specified value to the end of the list.If the list is empty (head is None), we simply return, as there are no duplicates to remove.Set current to head and create a set, seen_values, to store unique values we encounter. We start by adding the value of the first node (current.value) to it. Then Loop through list and the method prints each value in the linked list, following arrows (" -> ") to indicate the links between nodes. It ends with "None" to show the list’s end and method prints each value in the linked list, following arrows (" -> ") to indicate the links between nodes. It ends with "None" to show the list’s end.

## Exercise 4 [Add a method to merge two sorted linked lists into a single sorted linked list.]
implemented the merge_sorted_lists function to takes two sorted linked lists and merges them into a single sorted linked list, while loop continues as long as there are nodes in both list1 and list2, if list1's current node has a smaller value, we set current.next to list1 otherwise, we set current.next to list2. If one list is exhausted but the other still has nodes, we append all remaining nodes from that list to current.next since the list is already sorted, no further sorting is needed. The merged list starts at dummy.next, as dummy itself is an empty placeholder. Next the The merged list starts at dummy.next, as dummy itself is an empty placeholder and the while loop traverses each node until head is None, indicating the end of the list and also once the entire list is printed, it outputs None to signify the end.


# What I Implemented In Practical 6

## Exercise 1 [Implement a method to find the middle element of the linked list.]
Implemented the function if head is None (empty list), return None and slow and fast pointers both start at head which while loop fast and fast.next are not None, move slow one step forward (slow = slow.next) and fast two steps forward (fast = fast.next.next) which means slow moves at half the speed of fast, so when fast reaches the end of the list, slow will be in the middle. When the loop ends, slow will be pointing to the middle node and creating the linked list and finging middle node.

## Exercise 2 [Implement a method to find the middle element of the linked list.]
Implemented the function to checks whether a linked list has a cycle where parameter akes one parameter, head, which is the first node of the linked list and slow variable( pointer that moves one step at a time) & fast variable(pointer that moves two steps at a time). The while fast and fast.next loop continues as long as fast and fast.next are not None, which means it haven't reached the end of the list. If at any point slow equals fast, it indicates that there is a cycle in the list and if a cycle is detected, the function returns True and then if the loop terminates without finding a cycle it returns False, indicating that the linked list does not have a cycle. Since the linked list created (3 -> 2) does not have a cycle (the next of node2 is None), the output of print(has_cycle(node1)) will be False.

## Exercise 3 [Implement a method to remove duplicates from an unsorted linked list.]
I implement a method to remove duplicates values from the linked list and iIf the head of the list is None, that means there are no nodes, so it just returns None and if head of the list is None, that means there are no nodes, so it just returns None. then start by adding the first node’s value to the set, as it’s the first we encounter. The loop will continue as long as there is a next node to look at. When we reach the end of the list, current.next will be None, and the loop will stop. The function is to check if the next node’s value is in the set and remove the duplicate. If its not duplicate, it add the value of the next node to our set of seen values.

## Exercise 4 [Add a method to merge two sorted linked lists into a single sorted linked list.]
I implemented merge_sorted_list function merges two sorted linked lists into one sorted linked list then continue looping as long as both lists have nodes. If the value of the current node in list1 is smaller than that in list2 then attach list1 to the merged list (current.next = list1) and move the list1 pointer to the next node (list1 = list1.next).If the value in list2 is smaller or equal, attach list2 to the merged list and move the list2 pointer to its next node. After that if there are remaining nodes in either list1 or list2, we attach them to the end of the merged list.Finally, we return the merged list starting from the node after the dummy node (dummy.next). The function creates a linked list from a list of values(create_linked_list(values)). Used the function(print_linked_list), prints the entire linked list in a readable format.Moreover, We create two sorted linked lists from two lists of values: list1 with values [0,2,4] and list2 with values [1,3,5] and merge_two_sorted_lists function to merge list1 and list2. The result is stored in merged_list then print the merged linked list.


# What I Implemented In Practical 6

## Exercise 1 [Implement an in-place version of Quick Sort to improve its space efficiency.]
In this exercise the code implements the in-place Quick Sort algorithm by sorting the array in place. The quick_sort is recursive function [a function that repeats or uses its own previous term to calculate subsequent terms and thus forms a sequence of terms] that sorts the array by dividing it into smaller part, the function [if left < right:] it checks if it is false, the function stops, as the array or contains a single element where both are already sorted.The [pivot_array = division(arr, left, right)] function is  rearrange elements around a chosen pivot, which results in one element being in its correct sorted position then the quick_sort recursively sorts the left and right subarrays  leading to a fully sorted array by the time all recursive calls have returned. The devision function [def division(arr, left, right):], in this the last element (arr[right]) is choosen in the current section of the array as the pivot and next initialize i to left - 1, which keeps track of the position where the next element smaller than or equal to the pivot will be placed then each element arr[b] from left to right - 1, if it is smaller than or equal to the pivot, we increment i and swap arr[i] with arr[b] which ensures all the elements to the left of i are smaller than or equal to the pivot. Using the for loop, the pivot is placed in its correct sorted position by swapping arr[i + 1] with arr[right] that  divides the array into two sections: elements less than the pivot on the left and elements greater than the pivot on the right then the function returns the index i + 1, which is where the pivot now lies and the index split the array for further sorting.

## Exercise 2 [Modify Bubble Sort to stop early if the list becomes sorted before all passes are complete.]
I implemented the code that sorts the list of numbers using the Bubble Sort algorithm.Used [def bubble_sort(arr):] to  defines a function named bubble_sort that takes a list called arr as its input,[n = len(arr)] where n assigned the length of the list arr which tells how many elements are in the list, use the for loop [for i in range(n):] to run n times for each element in the list one time and the variable i is the loop counter, starting from 0 and going up to n-1.Within the loop the [swap = False] and within the for loop another for loop [for a in range(0, n - i - 1):] goes through the list where variable a is used to compare up to n - i - 1 because with each complete pass, the largest unsorted element "bubbles" to its correct position at the end of the list.

## Exercise 3 [Implement a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort or Quick Sort.]
I implemented the sort function for the sub arrays which sorts the array between left and right, also added time complexity for sub arrays. Used merge function to merge a left and a right subarray and merges them back into the main array arr between left and right and even made left_half and right_half to hold the two halves of arr between left and right and in the while loop which is a and b so that it keeps track of the current element in left_half and right_half, while k is the index in arr where elements are merged back..

## Exercise 4 [Create a visualization of how each sorting algorithm works using a library like Matplotlib.]
While coding I had to download matplotlib to plot the graphs and to visualize and imported random to  to generate random numbers for our array, simulating an unsorted list to be sorted. In the bubble_sort function, the algorithm repeat again through the list multiple times, comparing adjacent elements and swapping them if they are out of order, the [visualize_step(arr)] is the function that help to updates the visualization to show the array’s current state after each comparison and potential swap where function is passed as an argument from visualize_sorting, allowing us to see the sorting process in real-time. The visualization_sorting  initializes and manages the visualization by creating a figure and single set of axes for plotting the bars, creates bars representing each element in the array and sets the x-axis from 0-300 so all bars are displayed and then sets the y-axis above the max element in the bar. Next the visualization_step updates the height of the bars after sorting operation to reflect the current state of the array. [sort_func(arr, visualize_step)] this function sorts the passing arr and visualize_step where it updates the visualization each time a swap happens. The function[visualize_sorting(arr, bubble_sort)] used to show the sorting of arr using the bubble_sort function and then to display the plot with the function[plt.show]