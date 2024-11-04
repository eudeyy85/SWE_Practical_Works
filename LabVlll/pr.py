import matplotlib.pyplot as plt
import random
def bubble_sort(arr, visualize_step):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            visualize_step(arr)
def visualization_sorting(arr, sort_func):
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)   
    def visualize_step(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        plt.pause(0.5) 
    sort_func(arr, visualize_step)
arr = [random.randint(0, 300) for _ in range(15)]
visualization_sorting(arr, bubble_sort)
plt.show()


