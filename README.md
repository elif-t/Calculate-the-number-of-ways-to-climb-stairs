# Calculate-the-number-of-ways-to-climb-stairs

In this exercise, you will write a recursive function to solve a classic combinatorial problem: Climbing Stairs.

Imagine you are climbing a staircase. You have 
 steps to reach the top, and you can either take a single step or two steps at a time. Your task is to determine the number of distinct ways to reach the top of the staircase. For example:
- If there are 
 steps, you can reach the top in two ways: by taking two single steps, or by taking one double step.
- If there are 
 steps, you can reach the top in three ways: 
, 
, and 
.

Write a recursive function count_ways(n) that takes one parameter, n, which is the total number of steps to reach the top (an integer greater than or equal to 1). The function should return the number of ways as an integer.

To implement the count_ways(n) function, do as follows:

1. If n == 1, there is only 1 way (taking one single step).
2. If n == 2, there are 2 ways (either two single steps or one double step).
3. For n > 2, the number of ways to reach the top is the sum of the ways to reach n - 1 steps and n - 2 steps. This is because from the n-1 step, you can take a single step to reach n, and from the n-2 step, you can take a double step to reach n.

Requirements:
- The function should use recursion to solve the problem.
- You may not use loops or dynamic programming approaches.

Test your implementation with the provided print-function.
