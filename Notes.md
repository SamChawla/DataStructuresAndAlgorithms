# Notes 1.2

**Data Structures**: Different ways of organizing the data.
  
  The logical or mathematical model of a particular organization of data is called data structures.

e.g Queue [FIFO] , Stack [LIFO]

- There are many ways to solve a particular problem statement, but we have to find out the efficient way to solve that particular problem.

- There are mainly two important things to consider:
  - **Time Constraint**: Time taken to solve that particular problem considering the size of the input and algorithm we use.
  - **Space Constraint** : Memory allocation done for that particular problem or the amount of memory used for that problem.
  
- Asymptotic Notations:
  - **Big O Notation**: Defines the worst time constraint for a particular problem.
  - **&#937; Notation**: Defines the best case scenerio for that particular problem.

- Big O Notation is used to measure how running time or space requirements for your program grow as input size grows.

```python
time = a*n +b   
time = a*n # Keep Fastest growing term   
time = O(n) # Drop Constants
```

```python
def get_squared_numbers(numbers):
    # Time complexity is directly proportional 
    # to the length of list.
    squared_numbers = []
    for number in numbers:
        square_numbers.append(number*number)
    return squared_numbers

numbers = [2,5,8,9]
get_squared_numbers(numbers)
# Returns [4,25,64,81]
```
