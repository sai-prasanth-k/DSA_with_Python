# O(n^2)
def iterative_two_pointer(arr):
    target = 1401
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] + arr[j] == target:
                return [i, j]
            elif arr[i] + arr[j] > target:
                return -1


class BasicTwoPointer:
    arr: list[int] = [12, 112, 423, 54, 65, 474, 75, 86, 978, 52, 312]
    iterativeTwoPointerObj = iterative_two_pointer(arr)
    print(iterativeTwoPointerObj)
