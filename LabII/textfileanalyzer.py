#Step 1
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
    
content = read_file('sample.txt')
print(content[:300])

#Step 2
def count_lines(content):
    return len(content.split('\n'))

num_lines = count_lines(content)
print(f"Number of lines: {num_lines}")

#Step 3
def count_words(content):
    return len(content.split())

num_words = count_words(content)
print(f"Number of words: {num_words}")

#Step 4
from collections import Counter
def most_common_word(content):
    words = content.lower().split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

common_word, count = most_common_word(content)
print(f"Most common word: '{common_word}' (appears {count} times)")

#Step 5
def average_word_length(content) :
    words = content.split()
    word_lengths = [len(word) for word in words]
    return sum(word_lengths) / len(words) 

avg_length = average_word_length(content)
print(f"Average word length: {avg_length:.2f} characters")

# Step 6
def analyze_text(filename):
    content = read_file(filename)
    
    num_lines = count_lines(content)
    num_words = count_words(content)
    common_word, count = most_common_word(content)
    avg_length = average_word_length(content)
    
    print(f"File: {filename}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Most common word: '{common_word}' (appears {count} times)")
    print(f"Average word length: {avg_length:.2f} characters")
analyze_text('sample.txt')



#Exercise 1[Count the number of unique words]
def count_unique_words(word):
    words = word.split()
    unique_words = set(word)
    return len(unique_words)

text = read_file('sample.txt')
print("Number of unique words:", count_unique_words(text))



#Exercise 2[Find the longest word]
def find_longest_word(word):
    words = word.split()
    longest_word = max(words, key=len)
    return longest_word
text = read_file('sample.txt')
print("The longest word:", find_longest_word(text))



#Exercise 3[Count the occurrences of a specified word(case-insensitive)]
def count_specific_word(text, word):
    words = text.split()  
    count = words.count(word.lower())  
    return count

text = read_file('sample.txt')
word_to_count = 'the' 
print("Occurrences of 'the':", count_specific_word(text, word_to_count))



#Exercise 4[Calculate the percentage of words that are longer than the average word length.]
def percentage_of_long_words(text):
    words = text.split()
    if len(words) == 0:
        return 0.0
    average_length = sum(len(word) for word in words) / len(words)
    longer_words_count = sum(1 for word in words if len(word) > average_length)
    percentage = (longer_words_count / len(words)) * 100
    return percentage
text = read_file('sample.txt')
print(percentage_of_long_words(text)) 

