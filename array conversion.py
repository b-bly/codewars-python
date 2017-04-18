def array_conversion(arr):
  #coding and coding..

  sum = 0
  after_math = arr
  
  while len(after_math) > 1:
      after_sum = []
      for i in range(0, len(after_math), 2):
          sum = after_math[i] + after_math[i+1]
          after_sum.append(sum)
      after_math = []    
      after_math = after_sum
      product = 0
      after_product = []
      print(after_math)

      if len(after_math) <= 1: break
      
      for i in range(0, len(after_math)-1, 2):
          product = after_math[i] * after_math[i+1]
          after_product.append(product)
      after_math = []    
      after_math = after_product
      print(after_math)
  print(after_math)

array_conversion([1, 2, 3, 4, 5, 6, 7, 8])
print(len([186]))
