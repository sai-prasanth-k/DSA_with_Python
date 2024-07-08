

def basic_binary_search(arr, target, low, high):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return basic_binary_search(arr, target, low, mid-1)
        elif arr[mid] < target:
            return basic_binary_search(arr, target, mid+1, high)
        else:
            return -1


class BasicBinarySearch:
    arr = [1, 32, 53, 65, 24, 46, 67232, 3455, 65, 4232, 313, 647, 32, 1232]
    target = 647
    arr.sort()
    low = 0
    high = len(arr)-1
    basic_bs_method = basic_binary_search(arr, target, low, high)
    print(basic_bs_method)