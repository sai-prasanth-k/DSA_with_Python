from bisect import bisect_left, bisect_right


def bisect_binary_search(arr, target):
    # to find the leftmost insertion point of target
    i = bisect_left(arr, target)
    # to find the rightmost insertion point of target
    j = bisect_right(arr, target)-1
    if i and j != len(arr) and arr[i] and arr[j] == target:
        return i, j


class BisectBinarySearch:
    arr = [1, 32, 53, 65, 24, 46, 67232, 3455, 65, 4232, 313, 647, 32, 1232]
    target = 32
    arr.sort()
    print(arr)
    bisect_bs_obj = bisect_binary_search(arr, target)
    print(bisect_bs_obj)

