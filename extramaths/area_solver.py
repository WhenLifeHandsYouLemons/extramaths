# Imports
from math import pi, sin

# Area of a square
def area_square(length):
    area = length ** 2
    return area

# Area of a rectangle
def area_rect(height, width):
    area = height * width
    return area

# Area of a right-angled triangle
def area_right_angle_tri(base, height):
    area = (base * height) / 2
    return area

# Area of a non-right angled triangle
def area_non_right_angle_tri(a, b, C):
    area = 0.5 * a * b * sin(C)
    return area

# Area of a rhombus
def area_rhombus(D, d):
    area = (D * d) / 2
    return area

# Area of a trapezoid
def area_trapezoid(a, b, height):
    area = ((a + b) / 2) * height
    return area

# Area of a circle
def area_circle(r):
    area = pi * (r ** 2)
    return area
