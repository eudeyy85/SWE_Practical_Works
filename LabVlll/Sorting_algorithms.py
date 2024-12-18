# Step 1: Implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)

# Step 2: Implement Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)

# Step 3: Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)

# Step 4: Compare Performance
import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")
large_arr = [random.randint(1, 1000) for _ in range(1000)]
compare_sorting_algorithms(large_arr)

# Exercise 1
def quick_sort(arr, left, right):
    if left < right:
        pivot_array = division(arr, left, right)
        quick_sort(arr, left, pivot_array - 1)
        quick_sort(arr, pivot_array + 1, right)

def division(arr, left, right):
    a = arr[right]
    i = left - 1
    for b in range(left, right):
        if arr[b] <= a:
            i += 1
            arr[i], arr[b] = arr[b], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1 
arr = [20, 10, 15, 25, 0, 5]
quick_sort(arr, 0, len(arr) - 1)
print("The sorted array:", arr)

# Exercise 2
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap = False  
        for a in range(0, n - i - 1):
            if arr[a] > arr[a + 1]:
                arr[a], arr[a + 1] = arr[a + 1], arr[a]  
                swap = True  
        if not swap:
            break  
    return arr

arr = [9, 1, 6, 3, 12]
print("The sorted array:", bubble_sort(arr))

# Exercise 3
def sort(arr, left, right):
    for a in range(left + 1, right + 1):
        key = arr[a]
        b = a - 1
        while b >= left and arr[b] > key:
            arr[b + 1] = arr[b]
            b -= 1
        arr[b + 1] = key

def merge(arr, left, mid, right):
    left_half = arr[left:mid + 1]
    right_half = arr[mid + 1:right + 1]
    
    a = b = 0
    k = left
    
    while a < len(left_half) and b < len(right_half):
        if left_half[a] <= right_half[b]:
            arr[k] = left_half[a]
            a += 1
        else:
            arr[k] = right_half[b]
            b += 1
        k += 1
    
    while a < len(left_half):
        arr[k] = left_half[a]
        a += 1
        k += 1
    
    while b < len(right_half):
        arr[k] = right_half[b]
        b += 1
        k += 1

def merge_sort(arr, left, right, min_size=10):
    if left < right:
        if right - left + 1 <= min_size:
            sort(arr, left, right)
        else:
            mid = (left + right) // 2
            merge_sort(arr, left, mid, min_size)
            merge_sort(arr, mid + 1, right, min_size)
            merge(arr, left, mid, right)
arr = [48, 29, 43, 4, 8, 92, 12]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

# Exercise 4
