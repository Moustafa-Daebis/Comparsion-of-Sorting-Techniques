import random
import copy
import numpy as np
import sys
import time

print(sys.setrecursionlimit(2000))


def selection_sort(array, size):
    for i in range(0, size - 1):
        minimum = i
        for j in range(i + 1, size):
            if array[j] < array[minimum]:
                minimum = j
        if i != minimum:
            array[i], array[minimum] = array[minimum], array[i]


def insertion_sort(array, size):
    for i in range(1, size):
        key = array[i]
        hole = i
        while hole > 0 and array[hole - 1] > key:
            array[hole] = array[hole - 1]
            hole -= 1
        array[hole] = key


def merge_sort(array, first, last):
    if first < last:
        mid = (first + last) // 2
        merge_sort(array, first, mid)
        merge_sort(array, mid + 1, last)
        merge(array, first, mid, last)


def merge(array, nleft, mid, nright):
    length_left = mid - nleft + 1
    length_right = nright - mid
    left = [0] * length_left
    right = [0] * length_right
    for i in range(0, length_left):
        left[i] = array[nleft + i]
    for j in range(0, length_right):
        right[j] = array[mid + 1 + j]
    k = nleft
    i = 0
    j = 0
    while i < length_left and j < length_right:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    while i < length_left:
        array[k] = left[i]
        i += 1
        k += 1
    while j < length_right:
        array[k] = right[j]
        j += 1
        k += 1


def randomized_quicksort(thearray, first, last):
    if first < last:
        pivot = randomization(thearray, first, last)
        randomized_quicksort(thearray, first, pivot - 1)
        randomized_quicksort(thearray, pivot + 1, last)


def randomization(thearray, first, last):
    pivot = random.randint(first, last)
    thearray[last], thearray[pivot] = thearray[pivot], thearray[last]
    return partition(thearray, first, last)


def partition(thearray, first, last):
    pivot_value = thearray[last]
    i = first - 1
    for j in range(first, last):
        if thearray[j] <= pivot_value:
            i += 1
            thearray[i], thearray[j] = thearray[j], thearray[i]
    thearray[i + 1], thearray[last] = thearray[last], thearray[i + 1]
    return i + 1


# Main code execution
sample_number = int(input('Enter a  number of elements to generate a random array: '))
random_numbers = np.random.randint(1, 101, sample_number)
# generating 4 copies of the main array
copy1 = copy.deepcopy(random_numbers)
copy2 = copy.deepcopy(random_numbers)
copy3 = copy.deepcopy(random_numbers)
copy4 = copy.deepcopy(random_numbers)
# selection sort
begin1 = time.time()
selection_sort(copy1, len(copy1))
end1 = time.time() - begin1
# insertion sort
begin2 = time.time()
insertion_sort(copy2, len(copy2))
end2 = time.time() - begin2
# merge sort
begin3 = time.time()
merge_sort(copy3, 0, len(copy3) - 1)
end3 = time.time() - begin3
# randomized quick sort
begin4 = time.time()
randomized_quicksort(copy4, 0, len(copy4) - 1)
end4 = time.time() - begin4

print("original = ")
print(random_numbers)
print("-----------------")
print(copy1)
print(copy2)
print(copy3)
print(copy4)

print(f"Running time for Selection sort is {end1 * 1000} milliseconds")
print(f"Running time of the Insertion Sort is {end2 * 1000} milliseconds")
print(f"Running time for Merge Sort is {end3 * 1000} milliseconds")
print(f"Running time  for Quick sort {end4 * 1000} milliseconds")
