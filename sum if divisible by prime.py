

def sum_for_list(lst):
    # largest = find largest value in lst
    largest = max(lst)
    # p = [generate prime numbers somehow], from 2 to largest
    p = []
    count = 2
    
    while count < largest:
        isprime = True
        
        for x in range(2, int((count/2) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            p.append(count)
        
        count += 1
    
    # sum_list = factor, sum
    sum_list = []
    sum = 0
    #loop through prime array
    
    for j in p:
        #remember to reset sum!  Common error for me.
        sum = 0
        for i in lst:
        # loop through lst
            #if not lst[i] % p: (is divisible)
            if not i % j:
                sum += i
            # sum += lst[i]
            #sum_list.append([p, sum])
        sum_list.append([j, sum])
    #return list
    return sum_list
    
list = [12, 27, 15]
sum_for_list(list)
