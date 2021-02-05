'''
Ch 10: Common Sorting Algorithms

Piero Orderique
05 Feb 2021

Most used:
Merge Sort, Quick Sort, Radix Sort
'''
test1 = [10, 5, 4, 5, 2, 7, 1]
test2 = [23,5,32,5,2,3,5,7,3,5,4,35,3]

'''
Bubble Sort
Runtime: O(n^2) avg & worst case
Memory: O(1)

Start at beginning and swap the first two elements if the 1st is greater than 2nd
Then go on to next pair and so on and repeat until all elements are sorted
'''
def bubble_sort(arr) -> None:
    while True:
        isSorted = True
        for idx in range(0, len(arr) - 1):
            # swap if curr > next
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                isSorted = False

        if isSorted:
            break

'''
Selection Sort
Runtime: O(n^2)
Memory: O(1)

Find smallest elem w/linear scan and swap with the first element.
Repeat for rest of the list until all elems in place 
'''
def selection_sort(arr) -> None:
    pass

'''
MERGE SORT
Runtime: O(nlogn)
Memory: Depends

Divide arr in half, sort both, and merge them
'''
# *CTCI's implementation - memory: O(n) from helper
def merge_sort(arr):
    helper = [0]*len(arr)
    merge_sort(arr, helper, 0, len(arr) - 1)

def mergesort(arr, helper, low, high):
    if low < high:
        mid = int(low + (high - low) / 2)
        mergesort(arr, helper, low, mid) # sort left half
        mergesort(arr, helper, mid + 1, high) # sort right half
        merge(arr, helper, low, mid, high)

def merge(arr, helper, low, mid, high):
    # copy both halves into a helper array
    for idx in range(low, high+1):
        helper[idx] = arr[idx]

    helperLeft = low
    helperRight = mid + 1
    current = low

    # iterate through helper array. 
    # Compare left and right halves copying back the smaller element 
    # from the two halves into the original array
    while(helperLeft <= mid and helperRight <= high):
        if helper[helperLeft] <= helper[helperRight]:
            arr[current] = helper[helperLeft]
            helperLeft += 1
        else: # if right element is smaller than left
            arr[current] = helper[helperRight]
            helperRight += 1

        current += 1

    # copy the rest of the left side of the array into the target arr
    remaining = mid - helperLeft
    for idx in range(remaining + 1):
        arr[current + idx] = helper[helperLeft + idx]

    # No need to copy in right half becuase its already THERE!

'''
QUICK SORT
Runtime: O(nlogn) avg, O(n^2) worst case
Memory: O(logn)

Pick random element and partition the array such that all numbers that
are less than the partitioning element come before all elements that 
are greater than it. Keep partitioning until array is sorted
'''
# *CTCI's implementation
def quick_sort(arr):
    quicksort(arr, 0, len(arr) - 1)

def quicksort(arr, left, right):
    print(arr)
    idx = partition(arr, left, right)

    if left < idx - 1: # sort the left half
        quicksort(arr, left, idx - 1)
    if idx < right: # sort the right half
        quicksort(arr, idx, right)

def partition(arr, left, right):
    pivot = arr[left + (right - left) // 2] # pick pivot position
    while left <= right:
        # find element on left that should be on right
        while arr[left] < pivot: left += 1

        # find element on right that should be on left
        while arr[right] > pivot: right -= 1

        # swap the elements and move left and right indices
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left

'''
RADIX SORT
Runtime: O(kn)

Sorting Algo for integers (and some others) that takes advantage of the
fact that integers have a finitte number of bits.
We iterate through each digit of the number, grouping numbers by each digit.

Given array of ints, we might first sort by the first digit, so that the 0s
are grouped together. Then, we sort each of these groupings by the next digit.
We repeat this process sorting by each subsequent digit until array is sorted.

Average case runtime is O(kn) where k = # of passes of the sorting algorithm
'''
# TODO: FIND IMPLEMENTATION

###############    TESTING    ################
if __name__ == "__main__":
    quick_sort(test1)