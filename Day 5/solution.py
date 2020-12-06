#! /usr/bin/env python3

with open('Day 5/example_input', 'r') as f:
    example_input = [x.strip('\n') for x in f]
with open('Day 5/puzzle_input', 'r') as f:
    puzzle_input = [x.strip('\n') for x in f]

example = 0

def part1(data):
    ID = 0
    available = {k:[v for v in range (8)] for k in range (128)} # this is for part 2
    for element in data:
        row = [x for x in range(128)]
        col = [x for x in range(8)]
        for char in element:
            if char == 'F':
                row = row[:int(len(row)/2)]
            elif char == 'B':
                row = row[int(len(row)/2):]
            elif char == 'R':
                col = col[int(len(col)/2):]
            elif char == 'L':
                col = col[:int(len(col)/2)]
        available[row[0]].remove(col[0]) # removing occupied places from the available dict.
        if ID < row[0] * 8 + col[0]:    # grabbing the highest ID.
            ID = row[0] * 8 + col[0]
    for key,v in available.items():
        if len(v) == 1:
           part_2_ID = key * 8 + v[0] 
    return [ID, part_2_ID]

if __name__ == "__main__":
    if example:
        print(part1(example_input))
    print(f'The answer to part 1 is: {part1(puzzle_input)[0]}')
    print(f'The answer to part 2 is: {part1(puzzle_input)[1]}')