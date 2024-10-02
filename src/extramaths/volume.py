# Imports
from math import pi

def cube(length: float) -> float:
    """Calculates the volume of a cube.

    Args:
        length (float): The side length of the cube.

    Returns:
        float: The volume of the cube.
    """

    volume = length ** 3
    return volume

def cuboid(length: float, width: float, height: float) -> float:
    """Calculates the volume of a cuboid.

    Args:
        length (float): The length of the cuboid.
        width (float): The width of the cuboid.
        height (float): The height of the cuboid.

    Returns:
        float: The volume of the cuboid.
    """

    volume = length * width * height
    return volume

def prism(base: float, height: float) -> float:
    """Calculates the volume of a prism.

    Args:
        base (float): The area of the base of the prism.
        height (float): The height of the prism.

    Returns:
        float: The volume of the prism.
    """

    volume = base * height
    return volume

def pyramid(base: float, height: float) -> float:
    """Calculates the volume of a pyramid.

    Args:
        base (float): The area of the base of the pyramid.
        height (float): The height of the pyramid.

    Returns:
        float: The volume of the pyramid.
    """

    volume = (base * height) / 3
    return volume

def sphere(radius: float) -> float:
    """Calculates the volume of a sphere.

    Args:
        radius (float): The radius of the sphere.

    Returns:
        float: The volume of the sphere.
    """

    volume = (4 * pi * (radius ** 3)) / 3
    return volume
