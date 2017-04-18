import math
def is_square(n):
    
    root = math.sqrt(n)
    if root % 1:
        print( False)
    else:
        print (True)

is_square(4)
is_square(3)
