#! /usr/bin/env python3

# Don't mind me
'''
   N
W  +  E
   S
'''

directions = {
        "N": lambda distance: [0, distance],
        "E": lambda distance: [distance, 0],
        "S": lambda distance: [0,-distance],
        "W": lambda distance: [-distance, 0],
    }

def part1(actions):
    ship_coord = [0, 0]     # The ship will travel on a 2d axis. x = east/west - y = north/south 
    facing = 0              # Facing position is given in degrees. Facing = 0 means east. Facing = 180 means west.
    for action in actions:
        # First we check for the 4 directions and turning.
        if action[0] in directions:
            x, y= directions[action[0]](int(action[1:]))
            ship_coord = [ship_coord[0]+x, ship_coord[1]+y]
        elif action[0] == "L":
            facing += int(action[1:])
        elif action[0] == "R":
            facing -= int(action[1:])
        # If the action given is the "forward" action we simplify the value of "facing" 
        # to its equivalent between 0° and 360° if needed. 
        else:
            n = int(facing/360)
            if n > 0:
                facing -= n*360
            elif n < 0:
                facing -= n*360 # Careful with the signal here.

            # After the simplification, we just need to select the correct direction based on the "facing" value.
            if facing == 0:
                x, y= directions["E"](int(action[1:]))
                ship_coord = [ship_coord[0]+x, ship_coord[1]+y]
            elif facing == 90 or facing == -270:
                x, y= directions["N"](int(action[1:]))
                ship_coord = [ship_coord[0]+x, ship_coord[1]+y]
            elif facing == 180 or facing == -180:
                x, y= directions["W"](int(action[1:]))
                ship_coord = [ship_coord[0]+x, ship_coord[1]+y]
            elif facing == 270 or facing == -90:
                x, y= directions["S"](int(action[1:]))
                ship_coord = [ship_coord[0]+x, ship_coord[1]+y]

    return abs(ship_coord[0]) + abs(ship_coord[1])


def part2(actions):
    ship_coord = [0, 0]     # Knows where the ship is.
    waypoint = [10, 1]      # Contains how much and where the ship moves.
    for action in actions:
        if action[0] in directions:
            x, y= directions[action[0]](int(action[1:]))
            waypoint = [waypoint[0]+x, waypoint[1]+y]
        # Here we change the waypoint's direction.
        elif action[0] == "L":
            n = int(int(action[1:])/90)
            for _ in range(n):
                x, y = waypoint
                waypoint[0] = -y
                waypoint[1] = x
        elif action[0] == "R":
            n = int(int(action[1:])/90)
            for _ in range(n):
                x, y = waypoint
                waypoint[0] = y
                waypoint[1] = -x
        else:
            ship_coord[0] += waypoint[0] * int(action[1:])
            ship_coord[1] += waypoint[1] * int(action[1:])

    return abs(ship_coord[0]) + abs(ship_coord[1])

example = 0

if __name__ == "__main__":
    if example:
        with open("Day 12/example_input", "r") as f:
            example_input = f.read().splitlines()
        print(part1(example_input), '\nCorrect answer: 25')
        print(part2(example_input), '\nCorrect answer: 286')
    else:
        with open("Day 12/puzzle_input", "r") as f:
            puzzle_input = f.read().splitlines()
        print("Part 1 answer:", part1(puzzle_input))
        print("Part 2 answer:", part2(puzzle_input))
        