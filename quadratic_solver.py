"""Import square root function"""
from math import sqrt


def solve_quadratic(a, b, c):
    """Solve quadratic equation for a,b,c"""
    if a == 0:
        return []
    d = (b * b) - (4 * a * c)
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return [x1, x2]
    if d == 0:
        x = -b / (2 * a)
        return [x]
    return []
