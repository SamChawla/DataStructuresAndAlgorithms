# Notes

- Data Structures are building blocks or raw material for any software programs.
- The logical or mathematical model of a particular organization of data is called *data structures*.

- Big O Notation is used to measure how running time or space requirements for your program grow as input size grows.

```python
time = a*n +b  --> Keep Fastest growing term --> time = a*n --> Drop Constants --> time = O(n)
```

- Time complexity is directly proportional to the length of list.

```python
def get_squared_numbers(numbers):
    squared_numbers = []
    for number in numbers:
        square_numbers.append(number*number)
    return squared_numbers

numbers = [2,5,8,9]
get_squared_numbers(numbers)
# Returns [4,25,64,81]
```

- BigO refers to very large value. Hence if you have a function like,
