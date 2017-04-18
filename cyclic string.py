#Cyclic string

def cyclic_string(s):
    
    for i in range(1, len(s)+1):
        substring = s[0:i]
        pattern = True
        for j in range(0, len(s)):
            if (s[j] != substring[j % len(substring)]):
                pattern = False
                break
        if pattern: return i



s = 'abcabc'
def cyclic_string2(s):
  for i in range(1, len(s)):
      #i = 1
      if (s[:i] * (len(s) // i + 1))[:len(s)] == s:
          # 'a'  *  7               )[:6] == 'abcabc'
          # 'ab' * 4
          # 'abc' * 3
          return i
  
print('ab')
