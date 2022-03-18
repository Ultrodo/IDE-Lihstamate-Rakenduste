map1 = [
    [12, 0, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 0],   
    [1, 0, 0, 24],
    [1, 1, 1, 1]
]
map2 = [
    [12, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 1, 0],   
    [1, 0, 0, 24],
    [1, 1, 1, 1]
]
map = map1
# 1. step
start_position_x = 0
start_position_y = 0

def move(step, current_position_x, current_position_y):
    print("Current step is: ", step)
    print("current_position_y = ", current_position_y)
    print("current_position_x = ", current_position_x)
    can_move_right = current_position_x <= 2 and map[current_position_y][current_position_x + 1] == 0
    can_move_bottom = current_position_y <= 2 and map[current_position_y + 1][current_position_x] == 0

    if can_move_right:
        print("Should move right")
        current_position_x += 1
    if can_move_bottom:
        print("Should move down")
        current_position_y += 1

    return[current_position_x, current_position_y]
 
new_position = move(1, start_position_x, start_position_y)
new_position = move(2, new_position[0], new_position[1])
new_position = move(3, new_position[0], new_position[1])