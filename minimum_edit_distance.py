# Initialise the grid appropriately with the correct dimensions and initial values.
def init_grid(n, m, ins_cost, del_cost):
    grid = []
    for i in range(0,n):
        grid.append([])
        for j in range(0,m):
            grid[i].append([])

    for i in range(0,n):
        grid[i][0] = i * ins_cost

    for j in range(0,m):
        grid[0][j] = j * del_cost

    return grid

# Calculate the substitution cost, depending on whether we're substituting the same character or not.
def sub_cost_calc(char1, char2, sub_cost):
    if char1 == char2:
        return 0
    else:
        return sub_cost

# Populate the initialised grid with the correct values as per the words and costs entered.
def populate_grid(grid, word1, word2, sub_cost, ins_cost, del_cost):
    for i in range(1,len(word1)+1):
        for j in range(1, len(word2)+1):
            grid[i][j] = min(
                (grid[i-1][j]) + ins_cost,
                (grid[i][j-1]) +del_cost,
                (grid[i-1][j-1]) + sub_cost_calc(word1[i-1], word2[j-1], sub_cost)
            )
    return grid

# Collect input from the user, run the appropriate functions and then print the result.
def minimum_edit_distance():
    word1 = raw_input("First word: ")
    word2 = raw_input("Second word: ")
    sub_cost = input("Substitution cost: ")
    ins_cost = input("Insertion cost: ")
    del_cost = input("Deletion cost: ")
    should_print_grid = input("Print grid? 1 for yes: ")

    grid = init_grid(len(word1) +1, len(word2) +1, ins_cost, del_cost)
    populated_grid = populate_grid(grid, word1, word2, sub_cost, ins_cost, del_cost)

    if(should_print_grid == 1):
        print("Note: (0,0) is top left, (N,M) is bottom right.")
        print_grid(populated_grid)

    print("Minimum distance: {}".format(populated_grid[len(word1)][len(word2)]))

# Print the grid in a tabular for for ease of reading.
def print_grid(grid):
    for i in range(0, len(grid)):
        print(grid[i])

# Run minimum_edit_distance method when file is executed
minimum_edit_distance()