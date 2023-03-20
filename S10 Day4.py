# HACKER RANK DAY 4: BINOMIAL DISTRIBUTION I | 10 DAYS OF STATISTICS PROBLEM SOLUTION

"""In this Hackerrank Day 4: Binomial Distribution I 10 Days of Statistics problem we have
 Given The ratio of boys to girls for babies born in Russia is 1.09. If there is 1 child 
 born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, 
rounded to a scale of 3 decimal places."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

l, r = list(map(float, input().split(" ")))
odds = l / r
print(round(sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))


# HACKERRANK DAY 4: BINOMIAL DISTRIBUTION II | 10 DAYS OF STATISTICS PROBLEM SOLUTION

"""In this Hackerrank Day 4: Binomial Distribution II 10 Days of Statistics problem A manufacturer of 
metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they 
are incorrectly sized. What is the probability that a batch of 10 pistons will contain:

No more than 2 rejects?
At least 2 rejects?"""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))


# HACKERRANK DAY 4: GEOMETRIC DISTRIBUTION I | 10 DAYS OF STATISTICS PROBLEM SOLUTION

In this Hackerrank Day 4: Geometric Distribution I 10 Days of Statistics problem The 
probability that a machine produces a defective product is 1/3. What is the probability 
that the 1sth defect occurs in the 5th item produced?

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def geometric_distributon(n, p):
    return ((1-p)**(n-1))*p

a, b = list(map(int, input().split()))
n = int(input())
print('{:.3f}'.format(geometric_distributon(n, a/b)))

# HACKERRANK DAY 4: GEOMETRIC DISTRIBUTION II | 10 DAYS OF STATISTICS PROBLEM SOLUTION

"""In this Hackerrank Day 4: Geometric Distribution II 10 Days of Statistics problem The probability 
that a machine produces a defective product is 1/3. What is the probability that the 1st defect is
 found during the first 5 inspections?"""
 
 # PROBLEM SOLUTION IN PYTHON PROGRAMMING.

p=1/3

def geomprob(k,p):
    return p*(1-p)**(k-1)

print("{0:.3f}".format(sum([geomprob(k,p) for k in range(1,6)])))

