from helpers import helper
from collections import Counter

def make_lists(file):
    lines = [line.split() for line in file]
    left_nums = [int(line[0]) for line in lines]
    right_nums = [int(line[1]) for line in lines]
    
    return {"left_list": left_nums, "right_list": right_nums}

# Function computes part one
def total_distance(input_file):
    left_nums = make_lists(input_file)["left_list"]
    right_nums = make_lists(input_file)["right_list"]
    
    left_nums.sort()
    right_nums.sort()
    
    results = [abs(left-right) for left, right in zip(left_nums, right_nums)]
    
    return sum(results)

# Function computes part two
def similarity_score(input_file):
    # Count occurence of each number in left and right lists
    counts_left = Counter(make_lists(input_file)["left_list"])
    counts_right = Counter(make_lists(input_file)["right_list"])
    
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
    folder_name = input("Enter folder name: ")
    file_name = input("Enter file name: ")
    input_file = helper.read_file(folder_name, file_name)
    print(f"Part One: = {total_distance(input_file)}")
    print(f"Part Two: = {similarity_score(input_file)}")
    
if __name__ == "__main__":
    main()

