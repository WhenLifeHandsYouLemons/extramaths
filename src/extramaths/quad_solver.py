# Imports
from math import sqrt

# Quadratic solver
def quadraticsolver(a, b, c):
    value1 = ((b * -1) + sqrt((b * b) - (4 * a * c))) / (2 * a)
    value2 = ((b * -1) - sqrt((b * b) - (4 * a * c))) / (2 * a)
    
    return value1, value2
