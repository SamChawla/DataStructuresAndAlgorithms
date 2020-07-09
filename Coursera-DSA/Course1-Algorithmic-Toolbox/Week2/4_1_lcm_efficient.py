# python3
# Problem Statement: Given two integers a and b, find their least common multiple.
# Input: The two integers a, b are given in the same line separated by space.
# Output: LCM(a, b)


def gcd_eucledian(a, b):
    a, b = (a,b) if a>=b else (b,a)
    if b == 0:
        return a
    return gcd_eucledian(b, a%b)


def lcm(a, b):
    return int((a*b)/gcd_eucledian(a, b))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
