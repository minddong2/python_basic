square = [list(map(int,input().split())) for i in range(10)]
start_x, start_y = 1, 1
start_x, start_y = int(start_x), int(start_y)
feed = int(0)

while feed == 0:
    if square[start_x][start_y + 1] == 2:
        square[start_x][start_y+1] = 9 
        square[start_x][start_y] = 9
        start_y = start_y + 1
        feed = 1
        
    elif square[start_x][start_y + 1] == 0:
            if start_y + 1 <= 9:
                square[start_x][start_y+1] = 9
                square[start_x][start_y] = 9
                start_y = start_y + 1
                
    elif square[start_x+1][start_y] == 2:
        square[start_x+1][start_y] = 9
        square[start_x][start_y] = 9
        start_x = start_x + 1
        feed = 1
            
    elif square[start_x + 1][start_y] == 0:
        if start_x + 1 <= 9:
            square[start_x+1][start_y] = 9
            square[start_x][start_y] = 9
            start_x = start_x + 1
                
    elif square[start_x][start_y+1] == 1 and square[start_x+1][start_y] == 1:
        square[start_x][start_y] = 9
        feed = 1

for i in range(10):
    for j in range(10):
        print(square[i][j], end=' ')
    print()