from math import sqrt

def quadraticsolver(a, b, c):
    try:
        x1 = ((b * -1) + sqrt((b * b) - (4 * a * c))) / (2 * a)
        x2 = ((b * -1) - sqrt((b * b) - (4 * a * c))) / (2 * a)
        
        return x1, x2
    except ValueError:
        print("ValueError: Please input 3 numbers that will work.")