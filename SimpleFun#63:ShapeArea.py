def shape_area(n):
    a = 1
    b = 0
    i = 0
    if n == 1:
        return 1
    while n - 1 >= a:
        i = n + a
        a = a + 1
    b = n * i + 1
    b = b - n
    return b
