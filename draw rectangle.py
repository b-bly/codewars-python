def draw_rectangle(canvas, rectangle):
    x1 = rectangle[0]
    y1 = rectangle[1]
    x2 = rectangle[2]
    y2 = rectangle[3]

    #canvas [y][x]

    canvas[y1][x1] = canvas[y1][x2] = canvas[y2][x1] = canvas[y2][x2] = '*'

    for y in range(y1+1, y2):
        canvas[y][x1] = canvas[y][x2] = '|'

    for x in range(x1 + 1, x2):
        canvas[y1][x] = '-'
        canvas[y2][x] = '-'
    
    print(canvas)

canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
rectangle = [1, 1, 3, 3]

draw_rectangle(canvas, rectangle)

##[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
## ['a', '*', '-', '*', 'a', 'a', 'a', 'a'],
## ['a', '|', 'a', '|', 'a', 'a', 'a', 'a'],
## ['b', '*', '-', '*', 'b', 'b', 'b', 'b'],
## ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
>>> 
