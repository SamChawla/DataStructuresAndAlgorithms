# python3
# Problem Statement: Last Digit of the Sum of Squares of Fibonacci Numbers
# Compute the last digit of F0^2 + F1^2 + · · · + Fn^2.
# Input: Integer n.
# Constraints: 0 ≤ n ≤ 10^14.
# Output: The last digit of F0^2 + F1^2 + · · · + Fn^2.

def get_pisano_period(m):
    previous, current = 0, 1
    for count in range(0, m*m):
        previous, current = current, (previous + current) % m

        # Check for Pisano Period, It starts with 0, 1
        if (previous == 0 and current == 1):
            return count + 1


def get_fib_nth_value(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


def get_square_sum_fibonacci(n, m=10):
    pisano_period = get_pisano_period(m)
    fn = n % pisano_period
    fn1 = (n+1) % pisano_period
    fib_fn_last_digit = get_fib_nth_value(fn) % 10
    fib_fn1_last_digit = get_fib_nth_value(fn1) % 10
    return (fib_fn_last_digit * fib_fn1_last_digit) % 10


if __name__ == '__main__':
    n = int(input())
    # S[n^2] = F[n] * F[n+1]
    # Last Digit  => F[n] = F[n] % m
    print(get_square_sum_fibonacci(n))
