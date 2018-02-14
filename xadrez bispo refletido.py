def chess_bishop_dream(board_size, init_position, init_direction, k):
    finalpos = []
    for x in range(2):
        offset = (init_position[x]+(k*init_direction[x]))/board_size[x]
        if int(offset)% 2 == 0:
            finalpos.append(int(round((offset-int(offset))*board_size[x],0)))
            print('Pos '+str(x)+ ' é par! No teste da matriz '+ str(board_size))
        else:
            finalpos.append(int(round((((offset - int(offset)) * board_size[x])-(board_size[x]-1))*-1,0)))
            print('Pos ' + str(x) + ' é ímpar!No teste da matriz '+ str(board_size))
    print(finalpos)
    return finalpos



chess_bishop_dream([3, 7],[1, 2],[-1, 1],13) #0,1
chess_bishop_dream([1, 2],[0, 0],[1, 1],6)#,[0, 1])
chess_bishop_dream([2, 2],[1, 0],[1, 1],12)#,[1, 0])
chess_bishop_dream([1, 1],[0, 0],[1, -1],1000000000)#,[0, 0])
chess_bishop_dream([2, 3],[1, 2],[-1, -1],41)#,[0, 2])
chess_bishop_dream([17, 19],[14, 8],[1, -1],239239)#,[4, 17])
chess_bishop_dream([17, 19],[16, 18],[1, 1],239239239)#,[10, 2])

