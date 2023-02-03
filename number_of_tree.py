"""
Let suppose we have nxn grid and we have a tree which cover 2x2 grid when we plant it. How much trees we can plant for n input.  
"""
#Solution:
print(((n-n%2)//2)**2)
