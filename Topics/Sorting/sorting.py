# Sorting Algorithms

def bubble_sort(arr):
    total = len(arr)

    for i in range(total-1):
        for j in range(total-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def selection_sort(arr):
    total = len(arr)
    for i in range(total-1):
        min_index = i
        for j in range(min_index+1, total):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        while j >= 0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = anchor


def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start+=1

        while elements[end] > pivot:
            end-=1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


if __name__ == '__main__':
    arr = [1, 9, 3, 2, 5, 4, 6]

    bubble_sort(arr)
    print(f"Bubble Sort: {arr}")

    arr1 = [1, 9, 3, 2, 5, 4, 6, 0]
    selection_sort(arr1)
    print(f"Selection Sort: {arr1}")

    arr2 = [1, 9, 3, 2, 5, 4, 12]
    insertion_sort(arr2)
    print(f"Insertion Sort {arr2}")

    arr3 = [1, 9, 3, 2, 0, 4, 12]
    insertion_sort(arr3)
    print(f"Quick Sort {arr3}")
