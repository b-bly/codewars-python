def is_smooth(arr):
    d, m = divmod(len(arr), 2)
    print( arr[0] == arr[-1] == arr[d] + arr[d - 1] * (m == 0))

array = [2, 3, 2, 3, 2]
is_smooth(array)
