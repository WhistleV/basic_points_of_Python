# a * b
def multiply1(a, b):
    """
    a cant be zero, b must be a positive integer.
    return a * b
    """
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
def multiply2(a, b):
    """
    a cant be zero, b must be an integer.
    return a * b
    """
    if abs(b) == 1:
        if b == 1:
            return a
        elif b == -1:
            return -a
    elif b == 0:
        return b
    else:
        if b > 0:
            return a + multiply2(a, b - 1)
        elif b < 0:
            return -a + multiply2(a, b + 1)

# n!
def factorial(n):
    """
    n is a natural number.
    return n!
    """
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)