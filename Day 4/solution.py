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

example = 1

# It returns a list with each passport as an string element inside a list.
def data_parse(data):
    stk = list()
    parsed = list()
    for element in data:
        aux = ''
        if element != '':
            stk.append(element)
        elif element == '':
            while stk:
                aux += stk.pop() + ' '
            parsed.append(aux)
    while stk:
        aux += stk.pop() + ' '
    parsed.append(aux)
    return parsed
                

def part1(data):
    valid = 0
    full_pattern = ['(byr)', '(iyr)', '(eyr)', '(hgt)', '(hcl)', '(ecl)', '(pid)']
    for element in data:
        passed_tests = 0
        for pattern in full_pattern:
            if re.findall(pattern, element):
                passed_tests +=1
        if passed_tests == len(full_pattern):
            valid +=1
    return valid


if __name__ == "__main__":
    if example:
        assert part1(data_parse(example_input)) == 2
        print('Correct result on part 1 example!')
print(f'The answer to part 1 is: {part1(data_parse(puzzle_input))}')