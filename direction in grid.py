def direction_in_grid(n,m):
    #n = rows, m = columns
    # if rows == columns, turns = rows + columns - 2
    # if rows > columns, turns = rows + columns -2 - (rows - columns) * 2
    # if columns > rows, turns = rows + columns -3 - ((columns - 1) - rows) * 2
    # relative_turns = turns % 4
    # 0 R, 1, D, 2, L, 3, U
    
    direction_dict = {0:'R', 1: 'D', 2: 'L', 3: 'U'}

    if n == m:
        turns = n + m - 2
    elif n > m: 
        turns = n*2 - 1 - (n - m)*2
    else: 
        turns = 2 * m -2 - (m - n)*2

    turns = turns % 4
    print(turns, direction_dict[turns])
    return direction_dict[turns]

direction_in_grid(1,1)
direction_in_grid(2,2)
direction_in_grid(2,3)
direction_in_grid(2,4)
direction_in_grid(3,1)
direction_in_grid(100,100)
