# HACKERRANK DAY 8: LEAST SQUARE REGRESSION LINE | 10 DAYS OF STATISTICS SOLUTION

"""In this Hackerrank Day 8: Least Square Regression Line 10 Days of Statistics problem A group 
of five students enroll in Statistics immediately after taking a Math aptitude test. Each student's
 Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x,y) points:

(95,85)

(85,95)

(80,70)

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? 
Determine the equation of the best-fit line using the least-squares method, then compute and print the value of y 
when x=80."""

# PROBLEM SOLUTION IN PYTHON PROGRAMMING.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = 5
xy = [map(int, input().split()) for _ in range(n)]
sx, sy, sx2, sxy = map(sum, zip(*[(x, y, x**2, x * y) for x, y in xy]))
b = (n * sxy - sx * sy) / (n * sx2 - sx**2)
a = (sy / n) - b * (sx / n)
print('{:.3f}'.format(a + b * 80))
