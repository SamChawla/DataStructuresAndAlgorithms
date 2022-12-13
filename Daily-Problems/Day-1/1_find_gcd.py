# Find GCD using Euclid's Algorithm

# Steps:
# 1. For two integers a and b, if a>b, divide a by b and reminder is r.
# 2. If reminder 'r' is 0, then stop; our GCD is b.
# 3. Otherwise, set b to a, r to b and repeat step 1 untill r is 0.


def gcd(first, second):
    while second != 0:
        temp = first
        first = second
        second = temp % second
    return first


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_eucledian(a, b):
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd_eucledian(b, a % b)


if __name__ == "__main__":
    first_num = int(input("Enter First Number: "))
    second_num = int(input("Enter Second Number: "))
    ans_value = gcd(first_num, second_num)
    print("GCD for {} and {} is {}".format(first_num, second_num, ans_value))
