'''
stop_condition :

    all element in a line are equale
    OR
    all element in a column are equale
    OR
    all element in diagonal are equale

    To optimize :
    check only the changer line or column and the diagonal if the new element is in the diagonal

'''

grid = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]


grid_text = "|---|---|---|\n|   |   |   |\n|---|---|---|\n|   |   |   |\n|---|---|---|\n|   |   |   |\n|---|---|---|"
print(grid_text)
winning_condidtion = False

def print_grid(grid):
    print("|---|---|---|")
    print("| {} | {} | {} |".format(grid[0][0],grid[0][1],grid[0][2]))
    print("|---|---|---|")
    print("| {} | {} | {} |".format(grid[1][0],grid[1][1],grid[1][2]))
    print("|---|---|---|")
    print("| {} | {} | {} |".format(grid[2][0],grid[2][1],grid[2][2]))
    print("|---|---|---|")

def check_player_turn():
    pass

def check_cell_valid(grid, x, y):
    return grid[x-1][y-1] == 'O' or grid[x-1][y-1] == 'X'

while(not winning_condidtion):

    print("Enter your values")

    value = input().split(',')
    x, y, value_player = int(value[0]), int(value[1]), value[2]
    grid[x-1][y-1] = value_player
    print_grid(grid)
    line = all(eleme == value_player for eleme in grid[x-1][:])
    column = all(eleme == value_player for eleme in grid[:][y-1])
    diag = all(eleme == value_player for eleme in [grid[z][z] for z in range(3)])

    winning_condidtion = line or column or diag

    if  winning_condidtion :
        print("We have a winner")



