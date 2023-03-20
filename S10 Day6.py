# HACKERRANK DAY 6: THE CENTRAL LIMIT THEOREM I | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 6: The Central Limit Theorem I 10 Days of Statistics problem 
A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing
 49 boxes must be transported via the elevator. The box weight of this type of cargo follows 
 a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this 
 information, what is the probability that all 49 boxes can be safely loaded into the freight elevator
 and transported?"""
 
 # PROBLEM SOLUTION IN PYTHON PROGRAMMING.
 
 # Enter your code here. Read input from STDIN. Print output to STDOUT
import math

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))


# HACKERRANK DAY 6: THE CENTRAL LIMIT THEOREM II | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 6: The Central Limit Theorem II 10 Days of Statistics problem The number 
of tickets purchased by each student for the University X vs. University Y football game follows 
a distribution that has a mean of 2.4 and a standard deviation of 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. 
If there are only 250 tickets left, what is the probability that all 100 students will be able to 
purchase tickets?"""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

import math

numTic = float(input())
numStd = float(input())
mu = numStd * float(input())
sig = math.sqrt(numStd) * float(input())

print(round(0.5*(1+math.erf((numTic - mu)/(sig * math.sqrt(2)))),4))


# HACKERRANK DAY 6: THE CENTRAL LIMIT THEOREM III | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 6: The Central Limit Theorem III 10 Days of Statistics problem You have a sample 
of 100 values from a population with a mean of 500 and with a standard deviation of 80. Compute the interval 
that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that 
P(A<x<B)=0.95. Use the value of z=1.96."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
# true population distribution
mu, sigma = 500, 80

# sample mean distribution
muS, sigmaS = mu, sigma/(100**0.5)

# confidence intervals of sample mean dist
A = mu - (1.96*sigmaS)
B = mu + (1.96*sigmaS)

print(round(A,2))
print(round(B,2))