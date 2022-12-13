# python3
# Problem Statement: Given an integer n, find the last digit of the nth Fibonacci number Fn (that is, Fn mod 10).
# Input: An Integer n>=0
# Output: The last digit of Fn.


def get_fib_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10
    return current % 10


if __name__ == "__main__":
    n = int(input())
    print(get_fib_last_digit(n))
