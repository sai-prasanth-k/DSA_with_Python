# An array A with N elements is called a mountain if there is an index 'i'
# such that,
# A[0] < A[1] < A[2] < ... < A[i], and
# A[i+1] > A[i+2] > A[i+3] > ... > A[N-1]
# Here, the element at index is called the peak element of the mountain.
# Given an array A of N integers, A forms a mountain, write a program to find the index of peak element.
# Input
# First line contains a single integer N.
# Second line contains N space separated integers of A.
# Output
# Print a single integer representing the index of peak element.
# Constraints
# 1 <= N <= 3 * 10^5
# 1 <= A[i] <= 10^9
# Testcase 1
# Sample Input 1
# 6
# 1 2 3 5 3 2
# Sample Output 1
# 3
# Sample Input 2
# 4
# 1 4 3 2
# Sample Output 2
# 1
# This question is asked in following companies
# Amazon, Bloomberg, Facebook, Google, Microsoft, Quora, Uber
def peak_of_the_mountain(arr, n, low, high):
    if low >= high:
        return low
    mid = (low + high) // 2
    if mid < n - 1 and arr[mid] < arr[mid + 1]:
        return peak_of_the_mountain(arr, n, mid + 1, high)
    else:
        return peak_of_the_mountain(arr, n, low, mid)


def main():
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    result = peak_of_the_mountain(arr, n, 0, n - 1)
    print(result)


if __name__ == "__main__":
    main()
