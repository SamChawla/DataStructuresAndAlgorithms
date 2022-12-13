# python3
# Problem Statement: Given an integer n, find the last digit of the sum F0 + F1 + · · · + Fn
# Input: The input consists of a single integer n.
# Constraints:0 ≤ n ≤ 10^14
# Output: Output the last digit of F0 + F1 + · · · + Fn .


def get_pisano_period(m):
    previous, current = 0, 1
    for count in range(0, m * m):
        previous, current = current, (previous + current) % m

        # Check for Pisano Period, It starts with 0, 1
        if previous == 0 and current == 1:
            return count + 1


def get_fib_nth_value(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def last_digit_sum(n):
    pisano_period = get_pisano_period(10)
    # As per Formula: S(n) = F(n+2) -1
    n = (n + 2) % pisano_period
    return get_fib_nth_value(n) - 1


if __name__ == "__main__":
    n = int(input())
    print(last_digit_sum(n) % 10)
