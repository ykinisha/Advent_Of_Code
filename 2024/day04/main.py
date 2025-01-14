from helpers import helper

# Creates a 2D array/matrix
def make_grid(input_file) -> list[list]:
    grid = [line for line in input_file]
    return grid

# Display/print the puzzle or coordinates (row, col) positions
def show_grid(input_file: str, board: bool = True) -> None:
    grid = make_grid(input_file)
    height = len(grid)
    width = len(grid[0])
    for row in range(height):
        for col in range(width):
            if board:
                print(grid[row][col], end=" ")
            else:
                print((row, col), end=" ")
        print()
        
# XMAS begins with "X" hence begin search when letter is X
def is_valid(char: str, word: str) -> bool:
    """
    Checks if a character matches the first character of a given word.
    
    Args:
        char: The character to be checked.\n
        word: The word to be compared against.
    
    Returns:
        bool: True if the character matches the first character of the word,
        False otherwise.
    """
    return char == word[0]
        
# Checks word can fit horizontally to the right from a specified col position
def is_east_ok(word: str, col: int, width: int) -> bool:
    """
    Checks if the space to the right from a givem starting column is within the
    grid boundary.
    
    Args:
        word: Word that is being seacrhed.\n
        col: Starting column index.\n
        width: Number of columns or the total width available.
        
    Returns:
        bool: True if word can fit within horizontal boundary, otherwise False
    """
    space_span = width - col
    return len(word) <= space_span

# Checks word can fit horizontally to the left from a specified col position
def is_west_ok(word: str, col: int) -> bool:
    """
    Checks if the space to the left from a givem starting column is within the
    grid boundary.
    
    Args:
        word: Word that is being seacrhed.\n
        col: Starting column index.\n
        width: Number of columns or the total width available.
        
    Returns:
        bool: True if word can fit within horizontal boundary, otherwise False
    """
    space_span = col + 1
    return len(word) <= space_span

# Checks word can fit vertically upwards from a specified row position
def is_north_ok(word: str, row: int) -> bool:
    """
    Checks if a word can fit vertically upwards from a given starting row.
    
    Args:
        word: Word that is being seacrhed.\n
        row: Starting row index.\n
        
    Returns:
        bool: True if word can fit within vertical boundary, otherwise False.
    """
    space_span = row + 1
    return len(word)<= space_span

# Checks word can fit vertically downwards from a specified row position
def is_south_ok(word: str, row: int, height: int) -> bool:
    """
    Checks if a word can fit vertically upwards from a given starting row.
    
    Args:
        word: Word that is being seacrhed.\n
        row: Starting row index.\n
        height: Number of rows or the total height available.
        
    Returns:
        bool: True if word can fit within vertical boundary, otherwise False.
    """
    space_span = height - row
    return len(word) <= space_span

# Checks word can fit diagonally upwards to the right
def is_northEast_ok(word: str, row: int, col: int, width: int) -> bool:
    """
    Checks if a word can fit diagonally upwards to the right from a given
    starting position.
    
    Args:
        word: Word that is being seacrhed.\n
        row: Starting row index.\n
        col: Starting column index.\n
        width: Number of columns or the total width available.
        
    Returns:
        bool: True if the word can fit within the available rows upwards and
        columns to the right, False otherwise.
    """
    return is_north_ok(word, row) and is_east_ok(word, col, width)


# Checks word can fit diagonally downwards to the left
def is_southWest_ok(word: str, row: int, col: int, height: int) -> bool:
    """
    Checks if a word can fit diagonally downwards to the left from a given
    starting position.
    
    Args:
        word: Word that is being seacrhed.\n
        row: Starting row index.\n
        col: Starting column index.\n
        height: Number of rows or the total height available.
        
    Returns:
        bool: True if the word can fit within the available rows downwards and
        columns to the left, False otherwise.

    """
    return is_south_ok(word, row, height) and is_west_ok(word, col)


# Checks word can fit diagonally upwards to the left
def is_northWest_ok(word: str, row: int, col: int) -> bool:
    """
    Checks if a word can fit diagonally upwards to the left from a given
    starting position.
    
    Args:
        word: Word that is being seacrhed.\n
        row: Starting row index.\n
        col: Starting column index.\n
        
    Returns:
        bool: True if the word can fit within the available rows upwards and
        columns to the left, False otherwise.

    """
    return is_north_ok(word, row) and is_west_ok(word, col)


# Checks word can fit diagonally downwards to the right
def is_southEast_ok(word: str, row: int, col: int, height: int, width: int) -> bool:
    """
    Checks if a word can fit diagonally downwards to the right from a given
    starting position.
    
    Args:
        word: Word that is being seacrhed.\n
        row: Starting row index.\n
        col: Starting column index.\n
        height: Number of rows or the total height available.
        width: Number of columns or the total width available.
        
    Returns:
        bool: True if the word can fit within the available rows downwards and
        columns to the right, False otherwise.
    """
    return is_south_ok(word, row, height) and is_east_ok(word, col, width)

#----------------------------Part One------------------------------------------
## Option 1: increment using a counter
def count_xmas_1(input_file, word: str) -> int:
    grid = make_grid(input_file)
    height = len(grid) # number of rows
    width = len(grid[0]) # number of columns
    count = 0
    
    for row in range(height):
        for col in range(width):
            char = grid[row][col] # captures single character
            if is_valid(char, word): # Search if character is "X"
                
                # Check if subsequent letters are M, A, S and count
                if (is_east_ok(word, col, width) and
                    [grid[row][col+1], grid[row][col+2], grid[row][col+3]] == list(word[1:])):
                    count += 1
                    
                if (is_west_ok(word, col) and
                    [grid[row][col-1], grid[row][col-2], grid[row][col-3]] == list(word[1:])):
                    count += 1
                    
                if (is_north_ok(word, row) and
                    [grid[row-1][col], grid[row-2][col], grid[row-3][col]] == list(word[1:])):
                    count += 1
                    
                if (is_south_ok(word, row, height) and
                    [grid[row+1][col], grid[row+2][col], grid[row+3][col]] == list(word[1:])):
                    count += 1
                    
                if (is_northEast_ok(word, row, col, width) and
                    [grid[row-1][col+1], grid[row-2][col+2], grid[row-3][col+3]] == list(word[1:])):
                    count += 1
                    
                if (is_southWest_ok(word, row, col, height) and
                    [grid[row+1][col-1], grid[row+2][col-2], grid[row+3][col-3]] == list(word[1:])):
                    count += 1
                    
                if (is_northWest_ok(word, row, col) and
                    [grid[row-1][col-1], grid[row-2][col-2], grid[row-3][col-3]] == list(word[1:])):
                    count += 1
                    
                if (is_southEast_ok(word, row, col, height, width) and
                    [grid[row+1][col+1], grid[row+2][col+2], grid[row+3][col+3]] == list(word[1:])):
                    count += 1
                    
    return count

## Option 2: Find all words, store in a list and return size of list
def find_word_east(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving east from a starting position.
    
    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    # e.g. col is 6 and len is 4 word will be in index 6,7,8,9
    stop_pos = col + len(word)
    found = [grid[row][col_idx] for col_idx in range(col, stop_pos)]
    
    return found

def find_word_west(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving west from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list[str]: The list of characters forming the word found in the grid.
    """
    # Iterate backwards
    # e.g. col is 6 and len is 4 word will be in index 6,5,4,3
    stop_pos = col - len(word)
    found = [grid[row][col_idx] for col_idx in range(col, stop_pos, -1)]
    return found

def find_word_south(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving south from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    stop_pos = row + len(word)
    found = [grid[row_idx][col] for row_idx in range(row, stop_pos)]
    return found

def find_word_north(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving north from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    stop_pos = row - len(word)
    found = [grid[row_idx][col] for row_idx in range(row, stop_pos, -1)]
    return found

def find_word_northEast(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving northeast from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    stop_pos = col + len(word)
    
    # Column traverses from left to right while row decreases by 1
    found = []
    for col_idx in range(col, stop_pos):
        found.append(grid[row][col_idx])  # Start by appending the character at the current position
        row -= 1  # Move to the previous row
    
    return found

def find_word_southWest(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving southwest from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    stop_pos = col - len(word)
    
    # Column traverse from right to left while row increases by 1
    found = []
    for col_idx in range(col, stop_pos, -1):
        found.append(grid[row][col_idx])
        row += 1
        
    return found

def find_word_northWest(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving northwest from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    stop_pos = col - len(word)
    
    # Column traverse from right to left while row decreases by 1
    found = []
    for col_idx in range(col, stop_pos, -1):
        found.append(grid[row][col_idx])
        row -= 1
    
    return found

def find_word_southEast(row: int, col: int, grid: list[list], word: str) -> list:
    """
    Finds a word in a grid moving southeast from a starting position.

    Args:
        row: The starting row index.
        col: The starting column index.
        grid: The grid of letters.
        word: The word to find.

    Returns:
        list: The list of characters forming the word found in the grid.
    """
    stop_pos = col + len(word)
    
    # Column traverse from left to right while row increases by 1
    found = []
    for col_idx in range(col, stop_pos):
        found.append(grid[row][col_idx])
        row += 1
    
    return found


def count_xmas_2(input_file, word: str) -> int:
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

#----------------------------Part Two------------------------------------------

def is_diagonal_ok(word: str, row: int, col: int, width: int, height: int) -> bool:
    """
    Checks if a word can fit diagonally in all directions from a starting position.

    Args:
        word: The word to check.
        row: The starting row index.
        col: The starting column index.
        width: The width of the grid.
        height: The height of the grid.

    Returns:
        bool: True if the word can fit diagonally in all directions, False otherwise.
    """
    return (is_northEast_ok(word, row, col, width) and
            is_southWest_ok(word, row, col, height) and
            is_northWest_ok(word, row, col) and
            is_southEast_ok(word, row, col, height, width))

## Option 1 part 2: Counts if word fits diagonally in all directions
def count_mas_1(input_file, word: str) -> int:
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

## Option 2 for part 2 solution
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

