def array_change(list):

    moves = 0
    previous = list[0]
    for x in range(1, len(list)):
        diff = list[x]-previous
        if diff < 0:
            list[x] = previous + 1
            moves += -(diff) - 1
        elif diff == 0:
            list[x] = list[x] + 1
            moves += 1
        previous = list[x]
        
    print(moves)
    print(list)

array_change([-1000, 0, -2, 0])
