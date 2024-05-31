def iterative_binary_search(arr, target):
    low = 0
    high = len(arr)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            return -1


class IterativeBinarySearch:
    arr = [1, 32, 53, 65, 24, 46, 67232, 3455, 65, 4232, 313, 647, 32, 1232]
    target = 647
    arr.sort()
    iterative_bs_method = iterative_binary_search(arr, target)
    print(iterative_bs_method)
