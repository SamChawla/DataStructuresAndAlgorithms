# Find GCD using Euclid's Algorithm

# Steps:
# 1. For two integers a and b, if a>b, divide a by b and reminder is r.
# 2. If reminder 'r' is 0, then stop; our GCD is b.
# 3. Otherwise, set b to a, r to b and repeat step 1 untill r is 0.

def gcd(first, second):
    while(second!=0):
        temp = first
        first = second
        second = temp % second
    return first

if __name__ == "__main__":
    first_num = int(input("Enter First Number: "))
    second_num = int(input("Enter Second Number: "))
    ans_value = gcd(first_num, second_num)
    print("GCD for {} and {} is {}".format(first_num, second_num, ans_value))