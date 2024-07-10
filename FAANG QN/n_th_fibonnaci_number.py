# Fibonacci numbers are a sequence of numbers where a number F(i) is
# represented as F(i-1) + F(i+2)
# The following numbers are the initial
# numbers of Fibonacci sequence.
# 1, 1, 2, 3, 5, 8, 13, 21, ...
# Here, the Nth Fibonacci number is the Nth number from left in the
# sequence of Fibonacci numbers. For example, the fourth Fibonacci
# number is 3.
# Write a program to find the Nth number in the Fibonacci sequence.
# Input
# The only line of input contains a single integer N.
# Output
# Print a single integer representing the Nth number in the Fibonacci
# sequence.
# Explanation
# If N = 4,
# Firstly, we know that Fib(1) = 1 and Fib(2) = 1, now we can find Fib(3)
# using the mathematical representation mentioned in question text i.e.
# Fib(3) = Fib(2) + Fib(1) = (1 + 1) = 2.
# Similarly, Fib(4) = Fib(3) + Fib(2) = (2+1) = 3.
# Constraints
# 1 <= N <= 30
# Sample Input 1
# 2
# Sample Output 1
# 1
# Sample Input 2
# 4
# Sample Output 2
# 3
# This question is asked in following companies
# Amazon, Apple, Barclays, Bloomberg, Facebook, Mathworks, Microsoft, Yahoo, J.P. Morgan, SAP.




def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n-2)

def main():
    n = int(input())
    result = fibonacci(n)
    print(result)


if __name__ == "__main__":
    main()
