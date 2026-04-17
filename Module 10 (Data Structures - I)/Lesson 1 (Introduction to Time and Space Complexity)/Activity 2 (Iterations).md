# Asymptotic Analysis

## Asymptotic Breakdown
In this activity, $C$ represents various constants (the time taken for basic operations like assignment or addition). Here is how the functions translate into **Big O notation**:

### 1. Function 1: Constant Time
The number of operations is independent of $n$.
* **Mathematical Form:** $C_1$
* **Asymptotic Notation:** $O(1)$

### 2. Function 2: Linear Time
The number of operations grows in direct proportion to $n$.
* **Mathematical Form:** $C_2(n) + C_3$
* **Asymptotic Notation:** $O(n)$

### 3. Function 3: Quadratic Time
Because of the nested loop, the number of operations is related to the sum of the first $n$ integers:
$$\frac{n(n+1)}{2} = \frac{1}{2}n^2 + \frac{1}{2}n$$

* **Mathematical Form:** $C_4(n^2) + C_5(n) + C_6$
* **Asymptotic Notation:** $O(n^2)$

---

## Comparison of Outcomes
When comparing these, we look at the **growth rate**.

| If $n$ is... | $O(1)$ (Fun1) | $O(n)$ (Fun2) | $O(n^2)$ (Fun3) |
| :--- | :--- | :--- | :--- |
| **10** | 1 step | 10 steps | 100 steps |
| **1,000** | 1 step | 1,000 steps | 1,000,000 steps |
| **1,000,000** | 1 step | 1,000,000 steps | 1,000,000,000,000 steps |

> **The Outcome:** As $n$ increases, the performance gap becomes massive. **Function 1** is the most efficient because its execution time remains flat. **Function 3** is the least efficient because its execution time explodes as the input grows.