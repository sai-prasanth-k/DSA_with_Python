def pivot_element(arr, n, low, high):
    if low > high:
        return 0

    mid = (low + high) // 2
    if (mid < n - 1) and (arr[mid] > arr[mid + 1]):
        return mid + 1
    elif arr[low] <= arr[mid]:
        return pivot_element(arr, n, mid + 1, high)
    else:
        return pivot_element(arr, n, low, mid - 1)


def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    pivot = pivot_element(arr, n, 0, (n - 1))
    if pivot == 0:
        print(f"{arr[0]} {arr[n - 1]}")
    else:
        print(f"{arr[pivot]} {arr[pivot - 1]}")


main()
