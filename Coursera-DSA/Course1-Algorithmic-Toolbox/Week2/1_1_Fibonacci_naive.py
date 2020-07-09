# python3
# Problem Statement: Print the Fn for Fabonnaci Series.
# Input: An Integer n>=0
# Output: Fn


def fib_recurs(n):
    if n<=1:
        return n
    else:
        return fib_recurs(n-1) + fib_recurs(n-2)

if __name__ == '__main__':
    n = int(input("Enter the value of n:"))
    print(fib_recurs(n))
