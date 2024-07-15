# A rotated array is an array with its elements being shifted towards left
# or right by a 'some number' of indices. For example, if the array = {1, 2, 3, 4, 5}
#  and if it is rotated right by two indices, the resultant array = {4, 5, 1, 2, 3}
# Given an array A of N elements, A is sorted in increasing order and is
# rotated some number of times unknown to you beforehand. Write a
# program to find the smallest and the largest element of A.
# Input
# First line contains a single integer N.
# Second line contains N space-separated integers of A.
# Output
# Print two space-separated integers representing the smallest element
# and the largest element of A.
# Constraints
# 1 <= N <= 3* 10^5
# -10^9 <= A[i] <= 10^9
# Sample Input 1
# 6
# 5 6 1 2 3 4
# Sample Output 1
# 1 6
# Sample Input 2
# 7
# -2 -1 4 5 6 7 -3
# Sample Output 2
# -3 7
# This question is asked in following companies
# Amazon, Apple, Bloomberg, eBay, Facebook, Goldman Sachs, Google, Microsoft, Oracle, Uber, Walmart Labs


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
