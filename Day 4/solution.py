#! /usr/bin/env python3

import re

with open('Day 4/example_input', 'r') as f:
	example_input = [x.strip('\n') for x in f]
with open('Day 4/puzzle_input') as f:
	puzzle_input = [x.strip('\n') for x in f]

example = 0

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
                

def part1(data, restrict=0):
    valid = 0
    if restrict:    # this is for part 2
        full_pattern = [r'byr:[19]{2}[2-9]{1}\d|[20]{2}0[012]',
                        r'iyr:20(1[0-9]|20)',
                        r'eyr:20(2[0-9]|30)',
                        r'hgt:(1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in)',
                        r'hcl:#[a-f0-9]{6}\s',
                        r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
                        r'pid:\d{9}\s'
                        ]
    else:
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
print(f'The answer to part 2 is: {part1(data_parse(puzzle_input), 1)}')