from math import sqrt

mem = {}
def fibonacci(number: int) -> int:
    """Generates the nth number in the Fibonacci sequence (fib(n-1) + fib(n-2)).

    Args:
        number (int): The number in the Fibonacci sequence to generate. (Starting from 0)

    Returns:
        int: The nth number in the Fibonacci sequence.
    """

    if mem.keys().__contains__(number):
        return mem[number]

    if number <= 1:
        return 1
    else:
        total = fibonacci(number - 1) + fibonacci(number - 2)
        mem[number] = total

    return total

def quadratic(a: float, b: float, c: float) -> tuple:
    """Calculates the values of x in a quadratic equation (ax^2 + bx + c).

    Args:
        a (float): The coefficient of x^2.
        b (float): The coefficient of x.
        c (float): The constant.

    Returns:
        tuple: The values of x in the quadratic equation.
    """

    value1 = ((b * -1) + sqrt((b * b) - (4 * a * c))) / (2 * a)
    value2 = ((b * -1) - sqrt((b * b) - (4 * a * c))) / (2 * a)

    return value1, value2

def factorial(number: int) -> int:
    """Calculates the factorial of the given number (n!).

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.
    """

    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)

def _right_angle_trig(hypotenuse, opposite, adjacent, angle):
    if hypotenuse == None:
        print(hypotenuse)
    if opposite == None:
        print(opposite)
    if adjacent == None:
        print(adjacent)
    if angle == None:
        print(angle)

