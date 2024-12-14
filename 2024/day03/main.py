#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:25:28 2024

@author: ykinisha
"""
from helpers.helper import read_file
import re

def found_digits(file: str, pattern: str):
    prog = re.compile(pattern)
    total = 0
    for line in file:
        for found in prog.findall(line):
            x, y = (map(int, found))
            total += x * y
    
    return total

def found_digits_adjusted(file: str, pattern: str):
    total = 0
    enable = True
    prog = re.compile(pattern)
    for line in file:
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
    file = read_file("puzzle.txt")
    pattern_1 = r"mul\((\d{1,3}),(\d{1,3})\)"
    pattern_2 = r"(do\(\))|(don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"
    print(found_digits(file, pattern_1))
    print(found_digits_adjusted(file, pattern_2))
    
if __name__ == "__main__":
    main()




