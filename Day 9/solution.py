#! /usr/bin/env python3

example = 1

def part1(nums, size):
    pointer = 0 # this guy here is used in: nums[pointer:pointer+size]. Always selects the current valid group.
    test_pos = size # index for the current number under test.
    found = False
    while True:
        # Testing each number pair. If a pair is found, the flag is set to true and the pair search for the current number stops.
        # After that we test if the search ended with or without a success. If found == False, we return the test number. Else we
        # continue until the number is found or the list ends.
        for x in nums[pointer:pointer+size]:
            if (str(int(nums[test_pos]) - int(x)) in nums[pointer:pointer+size]) and ((int(nums[test_pos]) - int(x)) != int(x)):
                found = True
                break
        if test_pos == (len(nums) - 1):
            return "Not found"
        elif not found:
            return nums[test_pos]
        # Moving pointers foward and reseting the found flag.
        found = False
        pointer += 1
        test_pos += 1

def part2(nums, target):
    test = []
    aux = 0
    pointer = 0

    # Testing the numbers before the target.
    while True:
        if pointer == nums.index(target):
            pointer += 1
        else:    
            test.append(int(nums[pointer+aux]))
            if sum(test) == int(target):
                return test
            elif sum(test) > int(target):
                test = []
                pointer += 1
                aux = 0
            elif sum(test) < int(target):
                if aux < nums.index(target)-1:
                    aux += 1
                if aux == nums.index(target):
                    pointer += 1
                    aux = 0


if __name__ == "__main__":
    if example:
        with open("Day 9/example_input", "r") as f:
            example_input = f.read().splitlines()
            print("Part 1 example answer:", part1(example_input,5))
            print("Part 2 example answer:", part2(example_input, part1(example_input, 5)))
    with open("Day 9/puzzle_input", "r") as f:
        puzzle_input = f.read().splitlines()
        print("Part 1 puzzle answer:", part1(puzzle_input, 25))
        pt2_ans = part2(puzzle_input, part1(puzzle_input, 25))
        print("Part 2 puzzle answer:",pt2_ans[0]+pt2_ans[-1])