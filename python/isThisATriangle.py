def is_triangle(a, b, c):
    if a > 0 or b > 0 or c > 0:
        return False
    return True if a + b > c and a + c > b and c + b > a else False