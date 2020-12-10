#! /usr/bin/env python3
# Part 1 is a copy of https://github.com/VitaminJai solution because my logic was exatcly the same
# but his implementation is straightup better.
import re

def part1(rules, colour):
    ans = []
    for rule in rules:
        bag_pos = rule.find(' bags contain')
        if colour in rule[bag_pos:]:
            ans.append(rule[:bag_pos])
            ans.extend(part1(rules, rule[:bag_pos]))
    return ans

def part2(rules, colour):
    ans = 0
    pattern = re.compile(r'(\d) ([\w ]*) ')
    for rule in rules:
        if rule.startswith(colour):
            for found in pattern.finditer(rule):
                ans += int(found[1]) * (1 + part2(rules, found[2]))
    return ans

if __name__ == "__main__":
    example = 1
    if example:
        with open('Day 7/example_input', 'r') as f:
            example_input = f.read().split('\n')
        print(len(set(part1(example_input, 'shiny gold'))))
        print(part2(example_input, 'shiny gold'))
    
    with open('Day 7/puzzle_input', 'r') as f:
        puzzle_input = f.read().split('\n')
    print("Part 1:", len(set(part1(puzzle_input, 'shiny gold'))))
    print("Part 2:", part2(puzzle_input, 'shiny gold'))