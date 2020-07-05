# python3
# Problem Statement: Print the Fn for Fabonnaci Series.
# Input: An Integer n>=0
# Output: Fn


def get_fib_nth_value(n):
    if n <=1:
        return n

    previous = 0
    current = 1    
    
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


if __name__ == '__main__':
    n = int(input())
    print(get_fib_nth_value(n))
