import math
from math import sqrt
from fractions import Fraction
def multiply(m1, m2):
    x1, y1, z1 = m1
    x2, y2, z2 = m2
    
    result_x = x1*x2 - y1*z2 - z1*y2
    result_y = x1*y2 + y1*x2 - z1*z2
    result_z = x1*z2 + y1*y2 + z1*x2
    
    return (result_x, result_y, result_z)

def addition(m1, m2):
    x1, y1, z1 = m1
    x2, y2, z2 = m2
    
    result_x = x1+x2
    result_y = y1+y2
    result_z = z1+z2
    
    return (result_x, result_y, result_z)
result=multiply((3, -3, 3),(1, 2, 1))
print(result)
