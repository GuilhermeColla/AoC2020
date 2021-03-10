#! /usr/bin/env python3
'''
   N
W  +  E
   S
'''

def part1(actions):
    ship_coord = [0, 0]     # The ship will travel on a 2d axis. x = east/west - y = north/south 
    facing = 0              # The facing position is given in degrees. It increases in a clockwise manner.
                            # Facing = 0 means east. Facing = 180 means west.
    directions = {
        "N": lambda distance: [0, distance],
        "E": lambda distance: [distance, 0],
        "S": lambda distance: [0,-distance],
        "W": lambda distance: [-distance, 0],
    }
    for action in actions:
        # First we check for the 4 directions and turning.
        if action[0] in directions:
            x, y= directions[action[0]](int(action[1:]))
            ship_coord = [ship_coord[0]+x, ship_coord[1]+y]
        elif action[0] == "L":
            facing += int(action[1:])
        elif action[0] == "R":
            facing -= int(action[1:])
        # If the action given is the "forward" action we simplify the value of "facing" to its equivalent between 0° and 360° if needed. 
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


example = 0

if __name__ == "__main__":
    if example:
        with open("Day 12/example_input", "r") as f:
            example_input = f.read().splitlines()
        print(part1(example_input), '\n correct answer: 25')
    else:
        with open("Day 12/puzzle_input", "r") as f:
            puzzle_input = f.read().splitlines()
        print(part1(puzzle_input))
        