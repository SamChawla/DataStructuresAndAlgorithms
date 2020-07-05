# python3
# Problem Statement: Given two integers a and b, find their greatest common divisor.
# Input: The two integers a, b are given in the same line separated by space.
# Output: GCD(a, b)


def gcd_eucledian(a, b):
    a, b = (a,b) if a>=b else (b,a)
    if b == 0:
        return a
    return gcd_eucledian(b, a%b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd_eucledian(a, b))
