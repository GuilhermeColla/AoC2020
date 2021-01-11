#! /usr/bin/env python3

example = 0
puzzle = 1

def part1(adapters):
    adapters.sort() # sorting in crescent order
    adapters.insert(0, 0) # adding the wall socket
    adapters.append(adapters[-1]+3) # and the built-in charger to the list
    count = 0
    ans = {x+1:0 for x in range(3)} # dict containing the answers
    # each key in ans represents the possible diferences between adapters. We find what is said difference, and then add to the value
    # in the apropriate key.
    while count < (len(adapters)-1):
        ans[adapters[count+1]-adapters[count]] += 1
        count += 1
    return ans

def part2(adapters):
    # First I'm dividing the data into soubgroups. Each subgroup contains adapters with a difference of < 3 'jolts'.
    adapters.sort()
    adapters.insert(0, 0) # adding the outlet to the data.
    groups = [] # here we store said groups.
    for adapter in adapters:
        # This is just to start the process.
        if not groups:
            groups.append([adapter])
        else:
            # If the difference between the last adapter in the last subgroup is < 3, we add it to the subgroup.
            if adapter - groups[-1][-1] < 3:
                groups[-1].append(adapter)
            # If the difference is 3 (or more - not relevant here) we start a new subgroup.
            else:
                groups.append([adapter])
    
    # After obtaining 'grouped', we calculate the total possibilities.
    # To calculate said possibilities I've done some research to avoid getting into recursion.
    # For my puzzle input - as seen in part 1 - there's no difference of 2 between adapters, only differences of 1 and 3. Whith
    # that in mind, I found out that the folowing is true:
    # P(n) = 2^n, n <= 2
    # P(n) = 2^n - 3^(n-3), n > 2
    # with P(n) being the possible ways to arrange each subgroup with the problem's constraint, and 'n' being the length of the
    # subgroup minus the first and last adapters.
    # To get the total arrangements, we just multiply P(n) of each subgroup.
    total = 1
    for subgroup in groups:
        n = len(subgroup)-2 # subtracting the first and last adapters of each group. They MUST be in EVERY arrangement.
        if  n < 1: # when there's only 1 or 2 adapters in a subgroup, we pass because there's one possibility.
            pass
        elif n <= 2:
            total = total * (2**n)
        else:
            total = total * (2**n - 3**(n - 3))
    return total


if __name__ == "__main__":
    if example:
        with open("Day 10/example_input", "r") as f:
            example_input = list(map(int, f.read().splitlines()))
        print(part1(example_input))
        print(part2(example_input))
    if puzzle:
        with open("Day 10/puzzle_input", "r") as f:
            puzzle_input = list(map(int, f.read().splitlines()))
        print(part1(puzzle_input))
        print(part2(puzzle_input))