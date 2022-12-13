# python3
# Problem Statement: Given two integers n and m, output Fn mod m (that is, the remainder of Fn when divided by m)
# Input: The input consists of two integers n and m given on the same line (separated by a space).
# Constraints: 1 ≤ n ≤ 10^14 , 2 ≤ m ≤ 10^3 .
# Output: Output Fn mod m.


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


def get_fibonacci_modulo(n, m):
    pisano_period = get_pisano_period(m)
    n = n % pisano_period
    return get_fib_nth_value(n) % m


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(get_fibonacci_modulo(n, m))
