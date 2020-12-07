#! /usr/bin/env python3

with open("Day 6/example_input") as f:
    example_input = f.read().split('\n\n')
with open("Day 6/puzzle_input") as f:
    puzzle_input = f.read().split('\n\n')

example = 0

def part1(data):
    ans = 0
    for element in data:
        ans += len(set(element.replace('\n', '')))
    return ans

def part2(data):
    ans = 0
    groups = [element.split('\n') for element in data]
    for group in groups:
        ans += len(set.intersection(*[set(person) for person in group]))
    return ans

if __name__ == "__main__":
    if example:
        print(part1(example_input))
        print(part2(example_input))
    print(f'Part 1: {part1(puzzle_input)}')
    print(f'Part 2: {part2(puzzle_input)}')
