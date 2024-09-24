import random


random_list = [random.randint(1, 100) for _ in range(1000)]

#search algorithms
def linear_search(lst, target):
    """
    Linear search algorithm.
    """
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, target):
    """
    Binary search algorithm.
    """
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#sorting algorithms
def bubble_sort(lst):
    """
    Bubble sort algorithm.
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def quick_sort(lst):
    """
    Quick sort algorithm.
    """
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


sorted_list_bubble = bubble_sort(random_list.copy())
sorted_list_quick = quick_sort(random_list.copy())

print(sorted_list_bubble, sorted_list_quick[:10])
