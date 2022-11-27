# Find the sum of first n natural numbers.


def sum(n):
    """
    Return the sum of first n natural numbers
    >>> sum(10)
    55
    """
    sum = 0
    for val in range(1, n+1):
        sum +=val
    return sum


def sum_optimized(n):
    """
    Return sum of first n natural numbers
    Since the formula for this is: n(n+1)/2
    we will use the formula directly
    """
    return int(n*(n+1)/2)


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    print(sum(number))
    print(sum_optimized(number))
