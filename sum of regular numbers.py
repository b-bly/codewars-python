def sum_of_regular_numbers(arr):
    step_list = []
    for x in (1, len(arr)):
        step = arr[x] - arr[x - 1]
        step_list.append(step)

    sum_list = []
    current = step_list[0]
    count = 0
    previous_count = 1
    sum = 0
    
    for value in range(2, len(step_list)):
        if value == current:
            count += 1
            #increase count
        # elif count > 2
        
        elif count > 2:
            # add up stuff and put in [sum_list]
            for i in range(previous_count - 1, count - 1):
                sum += arr[i]
            sum_list.append(sum)
            previous_count = count
        #add up array values and return
            
    final_sum = 0
    for x in sum:
        final_sum += x
        
    return final_sum

sum_of_regular_numbers([-17, -9, 1, 9, 17, 4, -9])
