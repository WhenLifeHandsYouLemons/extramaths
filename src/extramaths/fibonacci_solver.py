def fibonacci(number):
    if number <= 1:
        return 1
    else:
        total = fibonacci(number - 1) + fibonacci(number - 2)
    return total
