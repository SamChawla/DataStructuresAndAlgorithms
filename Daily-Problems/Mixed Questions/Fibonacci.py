# python3
# Problem Statement: Print the Fn for Fabonnaci Series.
# Input: An Integer n>=0
# Output: Fn


def fib_recurs(n):
    """
    Naive Solution
    """
    if n <= 1:
        return n
    else:
        return fib_recurs(n - 1) + fib_recurs(n - 2)


def fib_list(n):
    """
    Improved Solution
    """
    fib_num_list = [0, 1]
    for val in range(2, n):
        fib_num_list.append(fib_num_list[val - 1] + fib_num_list[val - 2])
    return fib_num_list[-1]


def get_fib_nth_value(n):
    """
    Efficient Solution
    """
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


if __name__ == "__main__":
    n = int(input("Enter the value of n:"))
    print(fib_recurs(n))
