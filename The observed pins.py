#The observed pin
def get_pins(observed):

    possible_num_list = [['0', '8'],
    ['1', '2', '4'],
    ['1', '2', '3', '5'],
    ['2', '3', '6'],
    ['4', '1', '5', '7'],
    ['2', '4', '5', '6', '8'],
    ['3', '5', '6', '9'],
    ['4', '7', '8'],
    ['5', '7', '8', '9', '0'], 
    ['6', '8', '9']]
    varriations = []
    previous_varr = possible_num_list[int(observed[0])]
    
    # for loop over "observed" pin
    for i in range(1, len(observed)):
        varriations = []
        num = int(observed[i])
        possible_nums = possible_num_list[num]
        
        for k in range(0, len(previous_varr)):
            
            for j in range(0, len(possible_nums)):
                # need to erase varriations and rebuild each loop
                #build up the possible pin from the possible num list
                # store the growing string in a var
                # add the possible num[j] to it
                # append to variations_list
                next_num = possible_nums[j]
                new_varr = previous_varr[k] + next_num
                varriations.append(new_varr)
        previous_varr = varriations
            
    print(varriations)
  # return variations_list
  
get_pins('8')


#loop: number in observed
# ex. '1' of '11'
#possible_nums = possible_num_list[num]
    # loop: number in possible_nums ['1', '2', '4']
    # add possible num to each previous_nums
    # 11, 12, 14, 21, 22, 24, 41, 42, 44
    
