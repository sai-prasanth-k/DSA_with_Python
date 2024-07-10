# Peak elements of an array are the elements that are greater than their adjacent elements.
# The adjacent elements of an element at index are elements at index and . For corner elements
# Constraints
# 2 <= N <= 10^3
# -10^4 <= A[i] <= 10^4
# Sample Input 1
# 7
# 1 2 -1 3 1 10 1
# Sample Output 1
# Sample Output 1
# 1 3 5
# Sample Input 2
# 5
# 1 2 3 5 4
# Sample Output 2
# 3
# This question is asked in following companies
# Amazon, Apple, Bloomberg, Facebook, Google, Microsoft, Quora, Uber.

def peak_element_of_1D_array(arr, n):
    flag = 0
    for i in range(n):
        if i == 0 or i == n - 1:
            if i == 0:
                if arr[i] > arr[i + 1]:
                    print(i, end=" ")
                    flag = 1
            else:
                if arr[i] > arr[i - 1]:
                    print(i, end=" ")
                    flag = 1
        else:
            if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
                print(i, end=" ")
                flag = 1
    if flag == 0:
        print(-1)
    return


def main():
    n = int(input())
    list_element = list(map(int, input().strip().split()))[:n]
    peak_element_of_1D_array(list_element, n)
    return


if __name__ == "__main__":
    main()
