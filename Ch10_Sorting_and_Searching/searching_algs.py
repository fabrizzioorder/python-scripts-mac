'''
Binary Search
'''
def binary_search(arr, target) -> int:
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid # target found at this idx!

    return -1 # error!

def binary_search_recursive(arr, target, low, high):
    if low > high: return -1 # Error

    mid = low + (high - low) // 2

    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return mid # target found at this idx!


if __name__ == "__main__":
    test = [1,3,4,9,10,30,50,84,100]
    target = 84
    print(binary_search_recursive(test, target, 0 , len(test) - 1))