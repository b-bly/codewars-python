def array_manip(array):
    result = []
    least_greater = array[0]
    for i in range(len(array)):
        if i == len(array) - 1:
            break
        previous = array[i+1]
        for j in range(i+1, len(array)):
            if array[j] > array[i] and array[j] < previous:
                least_greater = array[j]
                previous = array[j]
            
            
            result.append(least_greater)
    print(result)

arr = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]
array_manip(arr)
