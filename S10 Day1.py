# HACKER RANK DAY 1: QUARTILES | 10 DAYS OF STATISTICS PROBLEM SOLUTION

"""In this Hackerrank Day 1: Quartiles 10 Days of Statistics problem we have 
Given an array of integers and we need to calculate the respective first quartile, 
second quartile, and third quartile. It is guaranteed that all the quartiles are integers."""


# Problem solution in Python programming.
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = sorted(list(map(int, input().split())))
from statistics import median
print(int(median(x[:n//2])))
print(int(median(x)))
print(int(median(x[(n+1)//2:])))

# HACKER RANK DAY 1: INTERQUARTILE RANGE | 10 DAYS OF STATISTICS PROBLEM SOLUTION

"""In this Hackerrank Day 1: Interquartile Range 10 Days of Statistics problem we have 
Given an array of integers and an array representing the respective frequencies of the first array's 
elements, construct a data set where each value occurs at a frequency given in array second. 
Then calculate and print the array's interquartile range, rounded to a scale of 1 decimal place."""

# Problem solution in Python programming.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st

n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]
N = sum(freq)
s.sort()

if n%2 != 0:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2+1:])
else:
    q1 = st.median(s[:N//2])
    q3 = st.median(s[N//2:])

ir = round(float(q3-q1), 1)
print(ir)

# HACKER RANK DAY 1: STANDARD DEVIATION | 10 DAYS OF STATISTICS PROBLEM SOLUTION

"""In this Hackerrank Day 1: Standard Deviation 10 Days of Statistics problem we have 
Given an array of integers, calculate and print the standard deviation. Your answer 
should be in decimal form, rounded to a scale of 1 decimal place"""

# Problem solution in Python programming.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())
X = [int(x) for x in input().strip().split()]

mean = sum(X) / n
variance = sum([((x - mean) ** 2) for x in X]) / n
stddev = variance ** 0.5

print("{0:0.1f}".format(stddev))



