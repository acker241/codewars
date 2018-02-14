def has_exit(maze):
    print(maze)
    def go_up(coords):
        if coords[0] == 0: #is at the top?
            return False
        elif maze[coords[0]-1][coords[1]] == space: return (coords[0]-1,coords[1])
        else: return False

    def go_down(coords):
        if coords[0] == maze_alt-1: #is at the bottom?
            return False
        elif maze[coords[0]+1][coords[1]] == space: return (coords[0]+1,coords[1])
        else: return False

    def go_left(coords):
        if coords[1] == 0: #is at the left?
            return False
        elif maze[coords[0]][coords[1]-1] == space: return (coords[0],coords[1]-1)
        else: return False

    def go_right(coords):
        if coords[1] == maze_larg-1: #is at the right?
            return False
        elif maze[coords[0]][coords[1]+1] == space: return (coords[0],coords[1]+1)
        else: return False


    def check_alternatives(coords):
        cposy,cposx = coords[0],coords[1]
        cpos = (cposy,cposx)
        all_alts = [go_up(cpos),go_down(cpos),go_left(cpos),go_right(cpos)]
        final = []
        for v_try in range(len(all_alts)):
            if all_alts[v_try] != False and visited.count(all_alts[v_try]) == 0:
                final.append(all_alts[v_try])
        return final

    maze_alt,maze_larg = len(maze), len(maze[0])
    katie,space,wall = 'k', ' ','#'
    k_count = 0
    wall_count = 0
    visited = []
    cp = []
    for coord_y in range(len(maze)):
        for coord_x in range(len(maze[coord_y])):
            if maze[coord_y][coord_x] == katie:
                k_count += 1
                k_coords = (coord_y,coord_x)
            elif maze[coord_y][coord_x] == wall:
                wall_count +=1
    if k_count != 1:
        if k_count > 1:
            raise Exception("There should be no multiple Kates")
        else: raise Exception("Not enough Kates")
    if wall_count == 0:
        return True

    k_cpos = k_coords
    visited.append(k_cpos)
    maze_exit = False
    while maze_exit == False:

        if k_cpos[0] == 0 or k_cpos[1] == 0 or k_cpos[0] == (maze_alt-1) or k_cpos[1] == (maze_larg-1):
            maze_exit = True
            break
        alternatives = check_alternatives(k_cpos)

        if len(alternatives) == 1:
            k_cpos = alternatives[0]
            visited.append(k_cpos)
            continue

        if len(alternatives)>1:
            next_step = alternatives[0]
            alternatives.pop(0)
            cp.append([k_cpos,alternatives])
            k_cpos = next_step
            continue

        if len(alternatives) == 0:
            if len(cp) < 1:
                return False
            else:
                last_cp = cp[len(cp)-1]
                last_cp_pos = last_cp[0]
                last_cp_alts = last_cp[1]
                next_step = last_cp_alts[len(last_cp_alts)-1]
                cp.pop(len(cp)-1)
                if len(last_cp_alts) == 1:
                    k_cpos = next_step
                    visited.append(k_cpos)
                    visited.append(last_cp_pos)
                    continue
                else:
                    last_cp_alts.pop(len(last_cp_alts)-1)
                    k_cpos = next_step
                    current_cp = [last_cp_pos,last_cp_alts]
                    cp.append(current_cp)
                    visited.append(k_cpos)

    if maze_exit == True:
        return True


maze1 = ["k"]
maze2 = ["###",
        "#k#",
        "###"]
maze3 = ["###",
        "#k ",
        "###"]
katies = ["k ",
        "kk"]
maze4 = ["########",
        "# # ####",
        "# #k#   ",
        "# # # ##",
        "# # # ##",
        "#      #",
        "########"]
maze5 = ["########",
        "# # ## #",
        "# #k#  #",
        "# # # ##",
        "# # #  #",
        "#     ##",
        "########"]

mazes = [maze1,maze2,maze3,maze4,maze5,katies]

for x in range(len(mazes)):

    print(has_exit(mazes[x]))

