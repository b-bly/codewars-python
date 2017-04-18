x = "*"
y = " "
n = 3
output = ""

def diamond(n):
    # Make some diamonds!
    output = ""
    if n <= 0 or not n % 2:
        return None
    
    for i in range(1, n+ 1, 2):
        num_spaces = int((n-i)/2) * " "
        stars = "*" * i
        output += num_spaces + stars + "\n"
        

    for i in range(n-2, 0, -2):
        num_spaces = int((n-i)/2) * " "
        stars = "*" * i
        output += num_spaces + stars + "\n"
    print(output)

diamond(5)

print(x.rjust(10))
