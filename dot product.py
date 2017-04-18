def dot_product(a, b):
    # your solution here
    product = sum([a[i]*b[i] for i in range(len(a))])
    
    print(product)

dot_product((2,0,-1),(0,-2,1))
