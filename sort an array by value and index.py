def sort_by_value_and_index(arr):
    arr_calc = map(lambda i,n: n * (i + 1), range(len(arr)), arr)
    return [x for (y,x) in sorted(zip(arr_calc, arr), key=lambda pair: pair[0])]


print(sort_by_value_and_index(arr))
