# Find Element in the 1D Array
# Solved Easy Helpful
# Given an array A of N integers and an integer K, A is sorted in
# increasing order, write a program to return the index of element K in
# A. Return -1 if K is not present in A.
# Input
# First line contains a single integer N.
# Second line contains N space-separated integers of A.
# Third line contains a single integer K.
# Output
# Print a single integer representing the index of element K in A.
# Suppose element K is not present in A, print -1.
# Constraints
# 1 <= N <= 3*10^5
# -10^9 <= A[i], K <= 10^9
# Sample Input 1
# 4
# 4 8 9 10
# 9
# Sample Output 1
# 2
# Sample Input 2
# 6
# -10 -8 -5 -1 5 6
# -1
# Sample Output 2
# 3
# This question is asked in following companies
# Amazon, Apple, Microsoft, Facebook, Paypal.

def linear_search(list_n, search_element):
    for i in range(0, len(list_n)):
        if list_n[i] == search_element:
            return i
    return -1


def main():
    n = int(input())
    list_n = list(map(int, input().strip().split()))[:n]
    search_element = int(input())
    print(linear_search(list_n, search_element))


if __name__ == "__main__":
    main()

