'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

def get_ways_recursive(n):
    return 0 if n < 0 else n if n < 2 else get_ways_recursive(n-1) + get_ways_recursive(n-2)

# This is why, for DP problems, you want to start with the most intuitive recursive solution!
# The recursive implementation shows that the solution is actually a fibonacci number.
# Therefore every implementation and performance test in algorithms/dynamic_programming/fibonacci.py
# applies.
