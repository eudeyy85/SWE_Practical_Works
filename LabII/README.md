# What I Implemented

# Exercise 1 [Modify the program to count the number of unique words in the text.]
While doing this exercise I implemented funtion that splits the input text(sample.txt) into list of individual words and spacing it.Next created a set  the list of words that contain the unique elements and remove the duplicates word and then used the function [len(unique_words)] to calculates the number of elements in the set, which is the count of unique words.

# Exercise 2 [Add a function to find the longest word in the text.]
While doing this exercise I implemented funtion that splits the input text(sample.txt) similar to exercise 1, used the [max(words, key=len)] to find the maximun element in the list of words and the key=len function specifies that the maximum element should be determined based on the length of each word.

# Exercise 3 [Implement a feature to count the occurrences of a specific word (case-insensitive).]
While doing this exercise I implemented function to split input text like in above exercises,used the function [words.count(word.lower())] to count() method of the list object to efficiently count the number of occurrences of the word'The/the' within the words list and the word would be treated as same word.

# Exercise 4 [Create a function to calculate the percentage of words that are longer than the average word length.]
While doing this exercise I implemented function [sum(len(word)] for word in words to calculate the total length of all the words, used [average_length = total_length / len(words)] calculates the average word length by dividing the total length by the number of words. Even used [longer_words_count = sum(1 for word in words if len(word) > average_length)] counts the number of words longer than the average length using a generator expression. Moreover, used the function [percentage = (longer_words_count / len(words)) * 100] to calculate the percentage of longestp ppppppppppwords by dividing the count of long words by the total number of words and multiplying by 100.

