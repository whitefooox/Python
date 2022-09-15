def triangle(a, b, c):
    if (a + b) > c and (b + c) > a and (a + c) > b:
        print('Это треугольник')
    else:
        print('Это не треугольник')

triangle(int(input()), int(input()), int(input()))