from math import pi, sin

def square(length: float) -> float:
    """Calculates the area of a square of the given side length.

    Args:
        length (float): The side length of the square.

    Returns:
        float: The area of the square.
    """

    area = length ** 2
    return area

def rectangle(height: float, width: float) -> float:
    """Calculates the area of a rectangle of the given height and width.

    Args:
        height (float): The height of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """

    area = height * width
    return area

def right_angle_triangle(base: float, height: float) -> float:
    """Calculates the area of a right-angled triangle of the given base and height.

    Args:
        base (float): The base length of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """

    area = (base * height) / 2
    return area

def triangle(a: float, b: float, C: float) -> float:
    """Calculates the area of a triangle of the given side lengths and angle.

    Args:
        a (float): One side length of the triangle.
        b (float): Another side length of the triangle.
        C (float): The angle between the two side lengths.

    Returns:
        float: The area of the triangle.
    """

    area = 0.5 * a * b * sin(C)
    return area

def rhombus(D: float, d: float) -> float:
    """Calculates the area of a rhombus of the given diagonals.

    Args:
        D (float): The first diagonal of the rhombus.
        d (float): The second diagonal of the rhombus.

    Returns:
        float: The area of the rhombus.
    """

    area = (D * d) / 2
    return area

def trapezoid(a: float, b: float, height: float) -> float:
    """Calculates the area of a trapezoid of the given base lengths and height.

    Args:
        a (float): The length of the first base of the trapezoid.
        b (float): The length of the second base of the trapezoid.
        height (float): The height of the trapezoid.

    Returns:
        float: The area of the trapezoid.
    """

    area = ((a + b) / 2) * height
    return area

def circle(r: float) -> float:
    """Calculates the area of a circle of the given radius.

    Args:
        r (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """

    area = pi * (r ** 2)
    return area

def circle(d: float) -> float:
    """Calculates the area of a circle of the given diameter.

    Args:
        r (float): The diameter of the circle.

    Returns:
        float: The area of the circle.
    """

    area = pi * ((d/2) ** 2)
    return area
