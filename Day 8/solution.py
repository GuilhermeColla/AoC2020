#! /usr/bin/env python3

example = 0

def part1(prog):
    acc = 0
    used = []
    line = 0 # Acts like a pointer.
    ended = True # Used in part 2.
    # Each command line implies in 2 elements inside the "prog" list. Inspite of that, we need to treat "line" with care. Every new 
    # command line, means line += 2. And the jmp command needs to accomodate that aswell by using twice the value given by the jmp command
    # This is needed because of the way I'm parsing the data here.
    while True:
        # Testing if the command has been run already.
        # For part 2, this detects if the program has ended due to a recursion or due to reaching the end.
        try:
            if line in used:
                ended = False
                break
            # If it's a new command, we identify it, and then read the next element in the list to get its value.
            # After that, we update the pointer (line).
            else:
                used.append(line)
            if prog[line] == "acc":
                acc += int(prog[line+1])
                line += 2
            elif prog[line] == "jmp":
                line += 2*int(prog[line+1])
            elif prog[line] == "nop":
                line += 2
        except IndexError:
            break
    return acc, ended

def part2(prog):
    current = 0 # This stores where we have already tried to substitute the command.
    first_try = True
    values = ["jmp", "nop"]
    # when first_try is True, we change values[0] for values[1]
    # when first_try is False, we reverse the values, and retry. After this, the program should end after second try.
    # If there's no answer, part2 returns "Not found"
    while True:
        try:
            test = prog.copy()
            aux = test.index(values[0], current+1)
            test.pop(aux)
            test.insert(aux, values[1])
            current = aux
            acc, flag = part1(test)
            if flag == True:
                return acc
        except ValueError:
            if first_try:
                values.reverse()
            else:
                return "Not found"


if __name__ == "__main__":
    if example:
        with open("Day 8/example_input", "r") as f:
            example_input = f.read().replace("\n"," ").split(" ")
            print("Part 1 example answer:", part1(example_input)[0])
            print("Part 2 example answer:", part2(example_input))
    
    with open("Day 8/puzzle_input", "r") as f:
        puzzle_input = f.read().replace("\n"," ").split(" ")
        print("Part 1 puzzle answer:", part1(puzzle_input)[0])
        print("Part 2 puzzle answer:", part2(puzzle_input))
