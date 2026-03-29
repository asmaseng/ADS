# task 1
def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)
    print(n, end=" ")


num = int(input())
print_numbers(num)


# task 2
def print_numbers_reversed(n):
    if n < 1:
        return

    print(n, end=" ")
    print_numbers_reversed(n - 1)


num = int(input())
print_numbers_reversed(num)


# task 3
def calculate_numbers(n):
    if n == 0:
        return 0
    return n + calculate_numbers(n - 1)


num = int(input())
print(calculate_numbers(num))


# task 4
def factorial_of_num(n):
    if n == 0:
        return 1
    return n * factorial_of_num(n - 1)


num = int(input())
print(factorial_of_num(num))

# task 5
a = int(input('Enter the num: '))
b = int(input('Enter the power: '))


def power_of_num(a, b):
    if b == 0:
        return 1
    return a * power_of_num(a, b - 1)


print(power_of_num(a, b))

# task 6
n = int(input())


def sum_of_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)


print(sum_of_digits(n))

# task 7
n = int(input())


def num_of_digits(n):
    if n == 0:
        return 0
    return 1 + num_of_digits(n // 10)


print(num_of_digits(n))

# task 8
n = int(input())


def reversed_number(n):
    if n == 0:
        return
    print(n % 10, end='')
    reversed_number(n // 10)


reversed_number(n)

# task 9
n = int(input())


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))

# task 10
word = input('enter your word: ')


def palindrome(word):
    return word == word[::-1]


print(palindrome(word))

# task 11
arr = list(map(int, input().split()))


def sum_of_array(arr, i=0):
    if len(arr) == i:
        return 0
    return arr[i] + sum_of_array(arr, i + 1)


print(sum_of_array(arr))

# task 12
arr = list(map(int, input().split()))


def max_of_array(arr, i=0):
    if len(arr) - 1 == i:
        return arr[i]
    max_rest = max_of_array(arr, i + 1)
    return arr[i] if arr[i] > max_rest else max_rest


print(max_of_array(arr))

# task 13
arr = list(map(int, input().split()))
target = int(input())


def count_occurences(arr, target, i=0):
    if i == len(arr):
        return 0
    if arr[i] == target:
        count = 1
    else:
        count = 0
    return count + count_occurences(arr, target, i + 1)


print(count_occurences(arr, target))

# task 14
arr = list(map(int, input().split()))
target = int(input())


def search(arr, target, i=0):
    if i == len(arr):
        return False
    if arr[i] == target:
        return True
    return search(arr, target, i + 1)


print(search(arr, target))

# task 15
arr = list(map(int, input().split()))


def sorted_list(arr, i=0):
    if len(arr) - 1 == i:
        return True

    if arr[i] > arr[i + 1]:
        return False

    return sorted_list(arr, i + 1)


print(sorted_list(arr))

# task 16
arr = list(map(int, input().split()))
target = int(input())


def search(arr, target, i=0):
    if i == len(arr):
        return -1
    if arr[i] == target:
        return i
    return search(arr, target, i + 1)


print(search(arr, target))