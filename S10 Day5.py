# HACKERRANK DAY 5: POISSON DISTRIBUTION I | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 5: Poisson Distribution I 10 Days of Statistics problem 
A random variable, x, follows a Poisson distribution with a mean of 2.5. Find 
the probability with which the random variable X is equal to 5."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial, exp

miu = float(input())
x = int(input())
poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)
print("%.3f" %poisson_prob)


# HACKERRANK DAY 5: POISSON DISTRIBUTION II | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 5: Poisson Distribution II 10 Days of Statistics problem a 
manager of an industrial plant is planning to buy a machine of either A or type B.
 on the first line we need to print the expected daily cost of machine A and on the
 second line, we need to print the expected daily cost of machine B."""
 
 # PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input from stdin
averageX, averageY = [float(num) for num in input().split(" ")]

# Cost
CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX, 3))
print(round(CostY, 3))


# HACKERRANK DAY 5: NORMAL DISTRIBUTION I | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 5: Normal Distribution I 10 Days of Statistics problem In a certain plant, 
the time taken to assemble a car is a random variable, X, having a normal distribution with a mean 
of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled 
at this plant in:

Less than 19.5 hours?
Between 20 and 22 hours?"""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean=20.0
stddev=2.0
h1=19.5
h21,h22=20.0,22.0

def integrate(func,b,n=10000):
    step=1/n
    if(b<0):step=-step
    n=int(abs(b)*n)
    a=0.0
    sq=0.0
    for _ in range(0,n):
        sq+=step*func(a)
        a+=step
    return abs(sq)

erf = lambda b : (2*math.pi**(-0.5)) * integrate(lambda x: math.exp(-x**2),b)
phi = lambda b : (1 + erf( (b-mean) / (stddev * 2**0.5) ))/2
lesh1 = phi(0.0) - phi(h1)
beth1h2 = phi(h22) - phi(h21)
print(f'{lesh1:.3f}')
print(f'{beth1h2:.3f}')

# HACKERRANK DAY 5: NORMAL DISTRIBUTION II | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 5: Normal Distribution II 10 Days of Statistics problem in the final grades for 
a physical exam taken by a large group of students have a mean of 70 and a standard deviation of 10. 
if we can approximate the distribution of these grades by a normal distribution, what percentage of the students

Score higher than 80.
Passed the test if the grade > 60.
Failed the test if the grade < 60."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))






