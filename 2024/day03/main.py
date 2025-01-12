from helpers import helper
import re

def found_digits(input_file: str, pattern: str) -> int:
    prog = re.compile(pattern)
    total = 0
    for line in input_file:
        for found in prog.findall(line):
            x, y = (map(int, found))
            total += x * y
            
    return total

def found_digits_adjusted(input_file: str, pattern: str) -> int:
    total = 0
    enable = True
    prog = re.compile(pattern)
    for line in input_file:
        for found in prog.findall(line):
            if "do()" in found:
                enable = True
            elif "don't()" in found:
                enable = False
            else:
                if enable:
                    x, y = (map(int, found[2:]))
                    total += x * y
                    
    return total

def main():
    folder_name = input("Enter folder name: ")
    file_name = input("Enter file name: ")
    input_file = helper.read_file(folder_name, file_name)
    pattern_1 = r"mul\((\d{1,3}),(\d{1,3})\)"
    pattern_2 = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    print("Part One: =", found_digits(input_file, pattern_1))
    print("Part Two: =", found_digits_adjusted(input_file, pattern_2))
    
if __name__ == "__main__":
    main()