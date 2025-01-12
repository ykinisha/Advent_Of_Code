from helpers import helper

# Validate list is sorted either ascending or descending
def is_sorted(a_list: list[int]) -> bool:
    """
    Checks if a given list of integers is sorted in either
    ascending or descending order
    
    Args:
        a_list: List of integers.
        
    Returns:
        bool: True if list is ascending or descending, otherwise False.

    """
    sort_asc =  all(a_list[i] <= a_list[i+1] for i in range(len(a_list)-1))
    sort_dsc =  all(a_list[i] >= a_list[i+1] for i in range(len(a_list)-1))
    
    return sort_asc or sort_dsc

# Validate adjaccent values differ by at least 1 and at most 3
def is_adjacent(a_list: list[int], min_diff: int, max_diff: int) -> bool:
    """
    Checks if difference between adjacent elements in list 
    increase or decrease within a specified range.
    
    Args:
        a_list: Input list of integers to be checked.\n
        min_diff: minimum allowed difference between adjacent values.\n
        max_diff: maximum allowed difference between adjacent values.
    
    Returns:
        bool: True if difference meets criteria, otherwise False.
    """
    
    for x, y in zip(a_list, a_list[1:]):
        if not (min_diff <= abs(x -y) <= max_diff):
            return False
    return True

#-------Part One-------
# Validate line is sorted and adjacent values meet criteria
def is_safe(a_list: list[int], min_diff: int, max_diff: int) -> bool:
    return is_sorted(a_list) and is_adjacent(a_list, min_diff, max_diff)

def count_safe(input_file: str, min_diff: int, max_diff: int) -> int:
    count_reports = 0
    for line in input_file:
        line = list(map(int, line.split()))
        if is_safe(line, min_diff, max_diff):
            count_reports += 1
            
    return count_reports

#-------Part Two-------
def is_safe_adjusted(a_list: [int], min_diff: int, max_diff: int) -> bool:
    if is_safe(a_list, min_diff, max_diff):
        return True
    else:
        for i in range(len(a_list)):
            new = a_list[:i] + a_list[i+1:] # Remove one element
            if is_safe(new, min_diff, max_diff):
                return True
        return False
    
def count_safe_adjusted(input_file: str, min_diff: int, max_diff: int) -> int:
    count_reports = 0
    for line in input_file:
        line = list(map(int, line.split()))
        if is_safe_adjusted(line, min_diff, max_diff):
            count_reports += 1
            
    return count_reports
        
   
def main():
    folder_name = input("Enter folder name: ")
    file_name = input("Enter file name: ")
    input_file = helper.read_file(folder_name, file_name)
    print("Part One: =", count_safe(input_file, min_diff=1, max_diff=3))
    print("Part Two: =", count_safe_adjusted(input_file, min_diff=1, max_diff=3))


if __name__ == "__main__":
    main()