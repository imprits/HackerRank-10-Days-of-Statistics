# HACKERRANK DAY 7: PEARSON CORRELATION COEFFICIENT I | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 7: Pearson Correlation Coefficient I  10 Days of Statistics problem 
You have given two n-element data sets, X and Y, to calculate the value of the Pearson correlation 
coefficient."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = list(map(float,input().strip().split()))
Y = list(map(float,input().strip().split()))

mu_x = sum(X) / N
mu_y = sum(Y) / N

stdv_x = (sum([(i - mu_x)**2 for i in X]) / N)**0.5
stdv_y = (sum([(i - mu_y)**2 for i in Y]) / N)**0.5


covariance = sum([(X[i] - mu_x) * (Y[i] -mu_y) for i in range(N)])

correlation_coefficient = covariance / (N * stdv_x * stdv_y)

print(round(correlation_coefficient,3))

# HACKERRANK DAY 7: SPEARMAN'S RANK CORRELATION COEFFICIENT | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 7: Spearman's Rank Correlation Coefficient I 10 Days of Statistics problem 
You have given two n-element data sets, X and Y, to calculate the value of Spearman's rank correlation 
coefficient."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
def get_rank(X, n):
    x_rank = dict((x, i+1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]
    
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

rx = get_rank(X, n)
ry = get_rank(Y, n)

d = [(rx[i] -ry[i])**2 for i in range(n)]
rxy = 1 - (6 * sum(d)) / (n * (n*n - 1))

print('%.3f' % rxy)


