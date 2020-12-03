#! /usr/bin/env python3

with open('Day 3/example_input', 'r') as f:
	example_input = [x.strip('\n') for x in f]
with open('Day 3/puzzle_input') as f:
	puzzle_input = [x.strip('\n') for x in f]

start_pos = (1, 1)	# (horizontal, vertical)
example = 0

def part1(slope, start, data):
	h_pos,v_pos = start
	mod = len(data[0])
	count = 0
	while h_pos <= len(data):
		if data[h_pos-1][(v_pos-1)%mod] == '#':
			count += 1
		h_pos += slope[0]
		v_pos += slope[1]
	return count


if __name__ == "__main__":
	if example:
		print(part1((1, 3), start_pos, example_input))
		assert part1((1, 3), start_pos, example_input) == 7
		print('Correct result on part 1 example!')
		assert part1((1, 1), start_pos, example_input) == 2
		assert part1((1, 3), start_pos, example_input) == 7
		assert part1((1, 5), start_pos, example_input) == 3
		assert part1((1, 7), start_pos, example_input) == 4
		assert part1((2, 1), start_pos, example_input) == 2
		print('Correct result on part 2 example!')
	print(f'Answer to part 1: {part1((1, 3), start_pos, puzzle_input)}')
	print(f'''Answer to part 2: { part1((1, 1), start_pos, puzzle_input)*
								  part1((1, 3), start_pos, puzzle_input)*
								  part1((1, 5), start_pos, puzzle_input)*
								  part1((1, 7), start_pos, puzzle_input)*
								  part1((2, 1), start_pos, puzzle_input)}''')