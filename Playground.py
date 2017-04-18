def triangular_one(n):
    triangle = 0
    increment = 0
    for i in range(0, n):
        increment = i + 1
        triangle += increment

    print(triangle)
    return triangle

#1,3,6, 10, 15, 21
#increment 2, 3, 4, 5, 6



def triangular(n):
    if n < 0:
        return 0
    triangle = int(n * (n + 1)/2)
    print(triangle)
    return triangle

triangular(9)
