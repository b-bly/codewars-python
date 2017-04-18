# Largest 5 digit number in a string of integers

def solution(digits):
    num = 0
    greatest = 0
    
    for i in range(0, len(digits)-4):
        offset = i + 5
        num = int(digits[i:offset])
 
        if num > greatest:
            greatest = num
    return greatest
    

solution("39273949382")

           

b 11
d < 17
d > 11
