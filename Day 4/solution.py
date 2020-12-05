#! /usr/bin/env python3

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
import re

with open('Day 4/example_input', 'r') as f:
	example_input = [x.strip('\n') for x in f]
with open('Day 4/puzzle_input') as f:
	puzzle_input = [x.strip('\n') for x in f]
# TODO: utilizar um stack para juntar os elementos da lista.
i = 0
parsed = list()
while i < len(example_input)-2:
    if (example_input[i] != '') and (example_input[i+1] != ''):
        parsed.append(example_input[i] + ' ' + example_input[i+1])
    i += 1
print(parsed)
print(example_input)
example = 1

def part1(data):
    valid = 0
    pattern = '(byr)|(iyr)|(eyr)|(hgt)|(hcl)|(ecl)|(pid)'
    for element in data:
        if element != '':
            pass


if __name__ == "__main__":
    if example:
        # assert part1(example_input) == 2
        print('Correct result on part 1 example!')