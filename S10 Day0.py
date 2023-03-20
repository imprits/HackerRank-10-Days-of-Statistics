

# HACKER RANK DAY 0: MEAN, MEDIAN, AND MODE | 10 DAYS OF STATISTICS SOLUTION

""" In this Hackerrank Day 0: Mean, Median, and Mode 10 Days of Statistics problem 
we have Given an array of integers, calculate and print the respective mean, median, 
and mode on separate lines. If your array contains more than one modal value, choose 
the numerically smallest one."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))


# HACKER RANK DAY 0: WEIGHTED MEAN | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 0: Weighted Mean 10 Days of Statistics problem we have 
Given an array of integers and an array representing the respective weights of 
the first array's elements, calculate and print the weighted mean of the first 
array's elements. Your answer should be rounded to a scale of 1 decimal place 
(i.e., 12.3 formats)."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))

