# python3
# Problem Statement: Given two integers a and b, find their greatest common divisor.
# Input: The two integers a, b are given in the same line separated by space.
# Output: GCD(a, b)


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd_naive(a, b))
