# Task 1: Print numbers from 1 to n
def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n - 1)
    print(n, end=" ")

# Task 2: Print numbers from n to 1
def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1(n - 1)

# Task 3: Sum of first n natural numbers
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

# Task 4: Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Task 5: Power (a^b)
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

# Task 6: Sum of digits
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)

# Task 7: Count digits
def count_digits(n):
    if n == 0:
        return 1
    return 1 + count_digits(n // 10) if n >= 10 else 1

# Task 8: Reverse number
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

# Task 9: Fibonacci (nth)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Task 10: Palindrome check
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

# Task 11: Sum of array
def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array(arr, n - 1)

# Task 12: Maximum in array
def max_array(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], max_array(arr, n - 1))

# Task 13: Count occurrences
def count_occurrences(arr, n, target):
    if n == 0:
        return 0
    count = 1 if arr[n - 1] == target else 0
    return count + count_occurrences(arr, n - 1, target)

# Task 14: Recursive linear search
def linear_search(arr, n, target):
    if n == 0:
        return False
    if arr[n - 1] == target:
        return True
    return linear_search(arr, n - 1, target)

# Task 15: Check if array is sorted
def is_sorted(arr, n):
    if n == 1:
        return True
    if arr[n - 1] < arr[n - 2]:
        return False
    return is_sorted(arr, n - 1)

# Task 16: Recursive binary search
def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, right, target)