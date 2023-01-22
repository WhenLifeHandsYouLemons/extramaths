# Imports
from math import pi

# Volume of a cube
def vol_cube(length):
    volume = length ** 3
    return volume

# Volume of a cuboid
def vol_cuboid(length, width, height):
    volume = length * width * height
    return volume

# Volume of a regular prism
def vol_prism(base, height):
    volume = base * height
    return volume

# Volume of any pyramid
def vol_pyramid(base, height):
    volume = (base * height) / 3
    return volume

# Volume of a sphere
def vol_sphere(radius):
    volume = (4 * pi * (radius ** 3)) / 3
    return volume
