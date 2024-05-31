def single_loop_two_pointer(arr, n, target):
    i = 0
    j = n - 1
    while j > i:
        if arr[i] + arr[j] == target:
            return i, j
        elif arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1
    return -1


class AdvancedTwoPointer:
    arr: list[int] = [12, 112, 423, 54, 65, 474, 75, 86, 978, 52, 312]
    arr_size = len(arr)
    arr.sort()
    target = 151
    singleLoopTwoPointerObj = single_loop_two_pointer(arr, arr_size, target)
    print(singleLoopTwoPointerObj)
