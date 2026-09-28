def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 
def binary_search(arr, target):
    low =0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 
    return -1
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    result = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i = i + 1
        else:
            result.append(right_half[j])
            j = j + 1
    while i < len(left_half):
        result.append(left_half[i])
        i = i + 1
    while j < len(right_half):
        result.append(right_half[j])
        j = j + 1
    return result
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = []
    middle = []
    right = []
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            middle.append(item)
        else:
            right.append(item)
    return quick_sort(left) + middle + quick_sort(right)
numbers = [42, 11, 88, 23, 7, 35]
print("Original list:", numbers)
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
target = 23
print("Linear Search for 23:", linear_search(numbers, target))
print("Binary Search for 23:", binary_search(sorted_numbers, target))
