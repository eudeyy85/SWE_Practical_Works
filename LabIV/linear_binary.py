

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
test_list = [3,1,4,1,5,9,2,6,5,3,5]
result = linear_search(test_list,6)
print(f"Linear search: Index of 6 is {result}")

#Step 2: Implement Binary Search

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted,6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

#Step 3: Compare Performance
import time

def compare_search_algorithms(arr, target):
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time

    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time

    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")
large_list = list(range(10000))
compare_search_algorithms(large_list,8888)

#Step 4: Implement Recursive Binary Search

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
result = binary_search_recursive(test_list_sorted,6,0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

#Step 5: Create a Main Function
def main():
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    target = random.choice(test_list) 
    print(f"\nSearching for: {target}")
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()


#Exercise 1
def linear_search_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices
arr = [1, 5, 7, 5, 2, 5, 8]
target = 5
print(linear_search_all(arr, target))

#Exercise 2
def binary_search_insert(arr, target):
    left, right = 0, len(arr)   
    while left < right:
        mid = (left + right) // 2       
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid   
    return left
arr = [1,2,3,4,5,7,8]
target = 6
num = binary_search_insert(arr, target)
print(f'The insertion point for a target value in a sorted list {target} is at index: {num}')

#Exercise 3
def count_comparisons(arr, target):
    c = 2
    for i in range(len(arr)):
        c += 4
        if arr[i] == target:
            return i, c
    return -2, c
arr = [-1,2,3,5,6]
target = 4
insertion_point, c = count_comparisons(arr, target)
print("Insertion point:", insertion_point)
print("Number of comparisons:", c)

#Exercise 4
import time

def linear_search(arr, target):
    try:
        return arr.index(target) 
    except ValueError:
        return -1 


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        left, right = (mid + 1, right) if arr[mid] < target else (left, mid - 1)
    return -1


def jump_search(arr, target):
    n = len(arr)
    s = int(n ** 1) 
    p = 0

    while arr[min(s, n) - 1] < target:
        p = s
        s += int(n ** 1)
        if p >= n:
            return -1

    for i in range(p, min(s, n)):
        if arr[i] == target:
            return i
    return -1

def measure_time(search, arr, target):
    start_time = time.time()
    result = search(arr, target)
    end_time = time.time()
    return result, end_time - start_time

size = 50000
arr = list(range(size)) 
target = size -6 
linear_result, linear_time = measure_time(linear_search, arr, target)
binary_result, binary_time = measure_time(binary_search, arr, target)
jump_result, jump_time = measure_time(jump_search, arr, target)
print(f"Linear Search: Found {linear_result} in {linear_time:.6f} seconds")
print(f"Binary Search: Found {binary_result} in {binary_time:.6f} seconds")
print(f"Jump Search: Found {jump_result} in {jump_time:.6f} seconds")

