from helpers import helper


def make_grid(input_file):
    grid = [list(line) for line in input_file]
    return grid

def show_grid(input_file):
    grid = make_grid(input_file)
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            #print(grid[row][col], end=" ")
            print((row, col), end=" ")
        print()

# check if a specific letter is present in a specific index of the word
## e.g XMAS begins with "X" hence begin search when letter is X
def is_valid(char, word):
    return char == word[0]


# Check if space is enough to search diagonally in the south east direction
def is_southEast_ok(word: str, row: int, col: int, height: int, width: int) -> bool:
    return is_south_ok(word, row, height) and is_east_ok(word, col, width)

def find_word_southEast(row: int, col: int, grid: list[list[int]], word: str) -> list[str]:
    stop_pos = col + len(word)
    
    # Col traverse from left to right while row increases by 1
    found = []
    for col_idx in range(col, stop_pos):
        found.append(grid[row][col_idx])
        row += 1
    
    return found

# Check if space is enough to search diagonally in the north west direction
def is_northWest_ok(word: str, row: int, col: int):
    return is_north_ok(word, row) and is_west_ok(word, col)

def find_word_northWest(row: int, col: int, grid: list[list[int]], word: str) -> list[str]:
    stop_pos = col - len(word)
    
    # Col traverse from right to left while row increases by 1
    found = []
    for col_idx in range(col, stop_pos, -1):
        found.append(grid[row][col_idx])
        row -= 1
    
    return found

# Check if space is enough to search diagonally in the south west direction
def is_southWest_ok(word: str, row: int, col: int, height: int):
    return is_south_ok(word, row, height) and is_west_ok(word, col)

def find_word_southWest(row: int, col: int, grid: list[list[int]], word: str) -> list[str]:
    stop_pos = col - len(word)
    
    # Col traverse from right to left while row increases by 1
    found = []
    for col_idx in range(col, stop_pos, -1):
        found.append(grid[row][col_idx])
        row += 1
        
    return found

# Check if space is enough to search diagonally in the north east direction
def is_northEast_ok(word: str, row: int, col: int, width: int):
    return is_north_ok(word, row) and is_east_ok(word, col, width)
        
def find_word_northEast(row: int, col: int, grid: list[list[int]], word: str) -> list[str]:
    stop_pos = col + len(word)
    
    # Col traverse from left to right while row decreases by 1
    found = []
    for col_idx in range(col, stop_pos):
        found.append(grid[row][col_idx]) # Start by appending "X"
        row -= 1 # go back to the previous row
    
    return found

# Check if space is enough to search upwadrs
def is_north_ok(word: str, row: int):
    space_span = row + 1
    return len(word)<= space_span

def find_word_north(row: int, col: int, grid: list[list[str]], word: str) -> list[str]:
    stop_pos = row - len(word)
    found = [grid[row_idx][col] for row_idx in range(row, stop_pos, -1)]
    return found
    
# Check if space is enough to search downwadrs
def is_south_ok(word: str, row: int, height: int):
    space_span = height - row
    return len(word) <= space_span

def find_word_south(row: int, col: int, grid: list[list[str]], word: str) -> list[str]:
    stop_pos = row + len(word)
    found = [grid[row_idx][col] for row_idx in range(row, stop_pos)]
    return found

# Check if space is enough to search left
def is_west_ok(word: str, col: int) -> bool:
    """
    Checks if the space to the left of the grid is within the grid boundary.
    
    Args:
        word: word that is being seacrhed.\n
        col: column index.\n
        
    Returns:
        bool: True if grid space is within boundary, otherwise False
    """
    space_span = col + 1
    return len(word) <= space_span

def find_word_west(row: int, col: int, grid: list[list[str]], word: str) -> list[str]:
    """
    Find a word to the left from a given position in a grid/matrix.
    
    Args:
        row: row index.\n
        col: column index.\n
        grid: puzzle grid.\n
        word: word that is being searched
        
    Returns:
        List of words that have been found.    
    """
    # Iterate backwards
    # e.g. col is 6 and len is 4 word will be in index 6,5,4,3
    stop_pos = col - len(word)
    found = [grid[row][col_idx] for col_idx in range(col, stop_pos, -1)]
    return found


# Check if space is enough to search right
def is_east_ok(word: str, col: int, width: int) -> bool:
    """
    Checks if the space to the right of the grid is within the grid boundary.
    
    Args:
        word: word that is being seacrhed.\n
        col: column index.\n
        width: number of columns
        
    Returns:
        bool: True if grid space is within boundary, otherwise False
    """
    space_span = width - col
    return len(word) <= space_span

def find_word_east(row: int, col: int, grid: list[list[str]], word: str):
    """
    Find a word to the right from a given position in a grid/matrix.
    
    Args:
        row: row index.\n
        col: column index.\n
        grid: puzzle grid.\n
        word: word that is being searched
        
    Returns:
        List of words that have been found.    
    """
    # e.g. col is 6 and len is 4 word will be in index 6,7,8,9
    stop_pos = col + len(word)
    found = [grid[row][col_idx] for col_idx in range(col, stop_pos)]
    
    return found
        

# Find all occurrences of XMAS store in a list and get length of the list
def count_xmas_1(input_file, word):
    grid = make_grid(input_file)
    height = len(grid) # number of rows
    width = len(grid[0]) # number of columns
    all_words = []
    
    for row in range(height):
        for col in range(width):
            char = grid[row][col] # captures single character
            if is_valid(char, word): # first character must be "X"
                
                if is_east_ok(word, col, width):
                    all_words.append(find_word_east(row, col, grid, word))
                
                if is_west_ok(word, col):
                    all_words.append(find_word_west(row, col, grid, word))
                
                if is_north_ok(word, row):
                    all_words.append(find_word_north(row, col, grid, word))
                    
                if is_south_ok(word, row, height):
                    all_words.append(find_word_south(row, col, grid, word))
                    
                if is_northEast_ok(word, row, col, width):
                    all_words.append(find_word_northEast(row, col, grid, word))
                    
                if is_southWest_ok(word, row, col, height):
                    all_words.append(find_word_southWest(row, col, grid, word))
                
                if is_northWest_ok(word, row, col):
                    all_words.append(find_word_northWest(row, col, grid, word))
                    
                if is_southEast_ok(word, row, col, height, width):
                    all_words.append(find_word_southEast(row, col, grid, word))
                    
    
    # Filter out invlaid words and retain XMAS
    all_words = [found for found in all_words if found == list(word)]
    return len(all_words)
            

def count_xmas_2(input_file, word):
    grid = make_grid(input_file)
    height = len(grid) # number of rows
    width = len(grid[0]) # number of columns
    count = 0
    for row in range(height):
        for col in range(width):
            char = grid[row][col]
            
            # Check character is "X"
            if is_valid(char, word):
                
                if is_west_ok(word, col):
                    if [grid[row][col-1], grid[row][col-2], grid[row][col-3]] == list(word[1:]):
                        count += 1
                
                if is_east_ok(word, col, width):
                    if [grid[row][col+1], grid[row][col+2], grid[row][col+3]] == list(word[1:]):
                        count += 1
                        
                if is_north_ok(word, row):
                    if [grid[row-1][col], grid[row-2][col], grid[row-3][col]] == list(word[1:]):
                        count += 1
                        
                if is_south_ok(word, row, height):
                    if [grid[row+1][col], grid[row+2][col], grid[row+3][col]] == list(word[1:]):
                        count += 1
                        
                if is_northEast_ok(word, row, col, width):
                    if [grid[row-1][col+1], grid[row-2][col+2], grid[row-3][col+3]] == list(word[1:]):
                        count += 1
                
                if is_southWest_ok(word, row, col, height):
                    if [grid[row+1][col-1], grid[row+2][col-2], grid[row+3][col-3]] == list(word[1:]):
                        count += 1
                
                if is_northWest_ok(word, row, col):
                    if [grid[row-1][col-1], grid[row-2][col-2], grid[row-3][col-3]] == list(word[1:]):
                        count += 1
                
                if is_southEast_ok(word, row, col, height, width):
                    if [grid[row+1][col+1], grid[row+2][col+2], grid[row+3][col+3]] == list(word[1:]):
                        count += 1
    
    return count


# Option 1 for part 2 solution
# Check s if all 4 diagonal directons are ok to search
def is_diagonal_ok(word, row, col, width, height):
    return (is_northEast_ok(word, row, col, width) and
            is_southWest_ok(word, row, col, height) and
            is_northWest_ok(word, row, col) and
            is_southEast_ok(word, row, col, height, width))

def count_mas_1(input_file, word):
    grid = make_grid(input_file)
    height = len(grid) # number of rows
    width = len(grid[0]) # number of columns
    count = 0
    for row in range(height):
        for col in range(width):
            char = grid[row][col]
            
            # Search for "A"
            if is_valid(char, word) and is_diagonal_ok(word, row, col, width, height):
                if (((grid[row-1][col-1] == "S" and grid[row+1][col+1] == "M") or \
                    (grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S")) and \
                    ((grid[row-1][col+1] == "S" and grid[row+1][col-1] == "M") or \
                    (grid[row-1][col+1] == "M" and grid[row+1][col-1] == "S"))):
                    count += 1
               
    return count

# Option 2 for part 2 solution
def count_mas_2(input_file, word):
    grid = make_grid(input_file)
    height = len(grid) # number of rows
    width = len(grid[0]) # number of columns
    count = 0
    for row in range(1, height-1): # Exclude first and last rows
        for col in range(1, width-1): # Exclude first and last columns
            char = grid[row][col]
            
            # Search for "A"
            if is_valid(char, word):
                if (((grid[row-1][col-1] == "S" and grid[row+1][col+1] == "M") or \
                    (grid[row-1][col-1] == "M" and grid[row+1][col+1] == "S")) and \
                    ((grid[row-1][col+1] == "S" and grid[row+1][col-1] == "M") or \
                    (grid[row-1][col+1] == "M" and grid[row+1][col-1] == "S"))):
                    count += 1
               
    return count


def main():
    folder_name = input("Enter folder name: ")
    file_name = input("Enter file name: ")
    input_file = helper.read_file(folder_name, file_name)
    word = "XMAS"
    part1_search_word = word
    part2_search_word = word[2:] # AS
    print("Part One (Option 1) =", count_xmas_1(input_file, part1_search_word))
    print("Part One (Option 2) =", count_xmas_2(input_file, part1_search_word))
    print("Part Two (Option 1) =", count_mas_1(input_file, part2_search_word))
    print("Part Two (Option 2) =", count_mas_2(input_file, part2_search_word))
    
if __name__ == "__main__":
    main()
