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


example = 0

if __name__ == "__main__":
    if example:
        with open("Day 13/example_input", "r") as f:
            example_input = f.read().splitlines()
            example_input[1] = example_input[1].replace("x,","").split(",")
        print(part1(example_input))
    else:
        with open("Day 13/puzzle_input", "r") as f:
            puzzle_input = f.read().splitlines()
            puzzle_input[1] = puzzle_input[1].replace("x,","").split(",")
        print(part1(puzzle_input))