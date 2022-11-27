# Algorithms

- [Algorithms](#algorithms)
  - [Definition](#definition)
    - [Properties of algorithms](#properties-of-algorithms)
  - [Steps to construct an algorithm](#steps-to-construct-an-algorithm)
  - [Analysis of Algorithms](#analysis-of-algorithms)
    - [Types of Analysis](#types-of-analysis)

## Definition

- It is a sequence of finite steps used to solve a particular problem.
e.g

```text
    Multiply(){
      1. Take 2 numbers (a,b)
      2. Multiply a and b and store in c.
      3. return c
}
```

### Properties of algorithms

- It should terminate after finite steps.
- It should produce atleast one output.
- It is independent of any programming language.
- It should be unabmbigious(Deteministic).

---

## Steps to construct an algorithm

1. Problem Definition
2. Design algorithm (Divide & Conquer, Greedy, DP and many more)
3. Draw Flow Chart
4. Testing
5. Implementation
6. Analysis (Time Complexing and Space Complexity)

---

## Analysis of Algorithms

Analysis can be done on the basis of:

- Time Complexity
- Space Complexity

Both time and space complexity can be calculated in terms of `Aysmptotic Notations`:

- __Big O (Worst Case Scenario)__
- Omega (Best Case Scenario)
- Theta (Average Case Scenario)

### Types of Analysis

- Apostiary analysis (Relative Ananlysis)
- Apriori Analysis (Absolute Analysis)

|Apostiary analysis|Apriori Analysis|
|:---:|:---:|
|Depends on hardware and language of compiler|Independs of hardware and language of compiler|
|We expect Exact Answers|We expect Approximate Answers|
|For every code we get different answers|We get same answers|
|Programs runs fast due to the hardware|Programs runs faster due to __good logic__|
