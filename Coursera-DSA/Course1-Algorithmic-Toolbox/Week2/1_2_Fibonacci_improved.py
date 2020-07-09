# python3
# Problem Statement: Print the Fn for Fabonnaci Series.
# Input: An Integer n>=0
# Output: Fn


def fib_list(n):
    fib_num_list = [0,1]
    for val in range(2,n):
        fib_num_list.append(fib_num_list[val-1] + fib_num_list[val-2])
    return fib_num_list[-1]


if __name__ == '__main__':
    n = int(input("Enter the value of n: "))
    print(fib_list(n))
