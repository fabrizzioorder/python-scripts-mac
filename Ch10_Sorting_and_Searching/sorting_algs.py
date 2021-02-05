'''
Ch 10: Common Sorting Algorithms

Piero Orderique
05 Feb 2021

Most used:
Merge Sort, Quick Sort, Radix Sort
'''
test1 = [10, 5, 4, 5, 2, 7, 1]
test2 = [23,5,32,5,2,3,5,7,3,5,4,84,35,3]

'''
Bubble Sort
Runtime: O(n^2) avg & worst case
Memory: O(1)

Start at beginning and swap the first two elements if the 1st is greater than 2nd
THen go on to next pair and so on and repeat until all elements are sorted
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

###############    TESTING    ################
if __name__ == "__main__":
    print(test1)
    bubble_sort(test1)
    print(test1)