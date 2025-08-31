# 3229.-Minimum-Operations-to-Make-Array-Equal-to-Target
# Minimum Operations to Transform Arrays

## Problem Statement

You are given two arrays: a **source** array and a **target** array, both of length `n`.
Your task is to determine the **minimum number of operations** needed to transform the source array into the target array.

In each operation, you may choose one of the following:

1. **Add 1 to any prefix** of the array (all elements from index `0` to some index `i`).
2. **Add 1 to any suffix** of the array (all elements from some index `i` to `n - 1`).

If it is impossible to transform the source array into the target array using these operations, return `-1`.

---

## Example

```text
Input:
n = 3
source = [1, 2, 2]
target = [2, 2, 3]

Process:
- Operation 1: Add 1 to prefix [0..0] → [1, 2, 2] → [2, 2, 2]
- Operation 2: Add 1 to suffix [2..2] → [2, 2, 2] → [2, 2, 3]

Output:
2
