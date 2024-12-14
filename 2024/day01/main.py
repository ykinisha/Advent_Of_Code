from helpers.helper import read_file
from collections import Counter

def make_lists(file):
    lines = [line.strip().split() for line in file]
    left_nums = [int(line[0]) for line in lines]
    right_nums = [int(line[1]) for line in lines]
    
    return {"left_list": left_nums, "right_list": right_nums}

# Function computes part one
def total_distance(input_file):
    left_nums = make_lists(input_file)["left_list"]
    right_nums =  make_lists(input_file)["right_list"]
    
    left_nums.sort()
    right_nums.sort()
    
    results = [abs(left-right) for left, right in zip(left_nums, right_nums)]
    
    return sum(results)

# Function computes part two
def similarity_score(file):
    # List of left and right numbers
    left = make_lists(file)["left_list"]
    right = make_lists(file)["right_list"]
    
    # Count occurence of each number in the left and right lists
    counts_left = Counter(left)
    counts_right = Counter(right)
    
    # Numbers will appear multiple times in each list
    # Each key in 'counts_left' will be multiplied by its value
    # Get the value in 'counts_right' if it contains the key from 'counts_left'
    scores = []
    for k in counts_left:
        score = k * counts_left.get(k) * counts_right.get(k, 0)
        if score != 0:
            scores.append(score)
            
    return sum(scores)

def main():
    puzzle = read_file("puzzle.txt")
    print(f"Part One: = {total_distance(puzzle)}")
    print(f"Part Two: = {similarity_score(puzzle)}")

if __name__ == "__main__":
    main()
