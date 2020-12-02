#! /usr/bin/env python3

with open(r"Day 1\example_input", "r") as f:
	example_input = [int(x.strip()) for x in f]
with open(r"Day 1\puzzle_input", "r") as f:
	puzzle_input = [int(x.strip()) for x in f]


target_prod=2020
example = 0

def part1(target, data):
	for x in data:
		if (target-x in data):
			return x, target-x

def part2(target, data):
    for x in data:
        for y in data:
            if (target - x - y) in data:
                return x, y, target-x-y

if __name__ == "__main__":
    if example:
        test_answer1 = part1(target_prod, example_input)
        assert test_answer1[0] * test_answer1[1] == 514579
        print('Correct result on part 1 example!')

        test_answer2 = part2(target_prod, example_input)
        assert test_answer2[0] * test_answer2[1] * test_answer2[2] == 241861950
        print('Correct result on part 2 example!')
    
    puzzle_ans = part1(target_prod, puzzle_input)
    print(f'Answer to part 1: {puzzle_ans[0] * puzzle_ans[1]}')
    puzzle_ans = part2(target_prod, puzzle_input)
    print(f'Answer to part 2: {puzzle_ans[0] * puzzle_ans[1] * puzzle_ans[2]}')