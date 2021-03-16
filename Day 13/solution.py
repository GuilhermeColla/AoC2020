#! /usr/bin/env python3


def part1(notes):
    bus = 0
    wait = 0
    arrival = int(notes[0])
    notes[1] = list(map(int,notes[1]))
    for bus_id in notes[1]:
        aux = int(arrival/bus_id)
        depart_time = aux*bus_id
        while depart_time < arrival:
            depart_time += bus_id
        if wait:
            if wait > (depart_time - arrival):
                wait = depart_time - arrival
                bus = bus_id
        else:
            bus = bus_id
            wait = depart_time - arrival
    return bus, wait, bus*wait

# I'll leave this here only because it works and it was my first attempt.
def part2_bruteforce(notes, start=0):
    busses = [[int(bus_id), notes.index(bus_id)] for bus_id in notes if bus_id != "x"]
    gold_time = int(start/busses[0][0])*busses[0][0]
    while True:
        print(gold_time)
        found = True
        for bus_data in busses:
            if (gold_time + bus_data[1]) % bus_data[0] == 0:
                continue
            else:
                found = False
                break
        if found:
            return gold_time
        else:
            gold_time += busses[0][0]


# Now I'll try to use the knowledge gathered.
# I ended up implementing what is said in this post:
# https://www.reddit.com/r/adventofcode/comments/kcb3bb/2020_day_13_part_2_can_anyone_tell_my_why_this/
def part2(notes):
    busses = [[int(bus_id), notes.index(bus_id)] for bus_id in notes if bus_id != "x"]
    i = 1
    base = int(busses[0][0])
    gold_time = 0
    while i < len(busses):
        while (gold_time + int(busses[i][1])) % int(busses[i][0]):
            gold_time += base
        base *= int(busses[i][0])
        i += 1
    return gold_time


example = 0

if __name__ == "__main__":
    if example:
        with open("Day 13/example_input", "r") as f:
            example_input = f.read().splitlines()
            example_part2 = example_input[1].split(",")
            example_input[1] = example_input[1].replace("x,","").split(",")
        # print(part1(example_input))
        print(part2(example_part2))
    else:
        with open("Day 13/puzzle_input", "r") as f:
            puzzle_input = f.read().splitlines()
            puzzle_part2 = puzzle_input[1].split(",")
            puzzle_input[1] = puzzle_input[1].replace("x,","").split(",")
        # print(part1(puzzle_input))
        print(part2(puzzle_part2))