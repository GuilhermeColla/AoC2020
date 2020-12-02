#! /usr/bin/env python3

with open(r"Day 2\example_input", "r") as f:
	example_input = [x.strip('\n').split(' ') for x in f]
with open(r"Day 2\puzzle_input", "r") as f:
	puzzle_input = [x.strip('\n').split(' ') for x in f]

example = 1

def part1(data):
    count = 0
    for element in data:
        min_val, max_val = element[0].split('-')
        char = element[1][0]
        pswrd = element[2]
        if int(min_val) <= pswrd.count(char) <= int(max_val):
            count += 1
    return count

def part2(data):
    count = 0
    for element in data:    # remember about python zero indexing!
        pos1, pos2 = element[0].split('-')
        char = element[1][0]
        pswrd = element[2]
        if (pswrd[int(pos1)-1] == char) ^ (pswrd[int(pos2)-1] == char):
            count += 1
    return count

if __name__ == "__main__":
    if example:
        assert part1(example_input) == 2
        print('Correct result on part 1 example!')
        assert part2(example_input) == 1
        print('Correct result on part 2 example!')
    print(f'Answer to part 1: {part1(puzzle_input)}')
    print(f'Answer to part 2: {part2(puzzle_input)}')
