#! /usr/bin/env python3
import copy

example = 0
puzzle = 1

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

def part1(ferry):
    original = copy.deepcopy(ferry) # needed because "original = ferry" doesn't create a new list.
    for row_number, row in enumerate(ferry):
        for seat_number, seat in enumerate(row):
            aux = 0 # counts occupied seats adjacent to the current seat.
            if seat == ".":
                pass
            else:
                # Need these conditions for the edges, because python returns a value for list[-1], and we
                # do not want that.

                # Taking the current seat as a reference:
                # Checking the tree seats above
                if row_number > 0 and (0 < seat_number < (len(row)-1)):
                    aux += original[row_number-1][seat_number-1:seat_number+2].count("#")
                # The tree seats below
                if row_number < (len(original)-1) and (0 < seat_number < (len(row)-1)):
                    aux += original[row_number+1][seat_number-1:seat_number+2].count("#")
                # The seat on the left
                if seat_number > 0:
                    aux += original[row_number][seat_number-1].count("#")
                # The seat on the right
                if seat_number < len(row)-1:
                    aux += original[row_number][seat_number+1].count("#")
                # Now the four corners of the matrix:
                # Leftmost seats
                if seat_number == 0:
                    # Checking the two seats below if not on the bottom row
                    if row_number != len(original)-1:
                        aux += original[row_number+1][:seat_number+2].count("#")
                    # Checking the two seats above if not on top row
                    if row_number != 0:
                        aux += original[row_number-1][:seat_number+2].count("#")
                # Rightmost seats
                if seat_number == len(row)-1:
                    # Checking two seats below if not on the bottom row
                    if row_number != len(original)-1:
                        aux += original[row_number+1][seat_number-1:].count("#")
                    # Checking two seats above if not on the top row
                    if row_number != 0:
                        aux += original[row_number-1][seat_number-1:].count("#")
                
                # Checking and changing the seat state, if needed.
                if seat == "L" and aux == 0:
                    ferry[row_number][seat_number] = "#"
                elif seat == "#" and aux > 3:
                    ferry[row_number][seat_number] = "L"

    # Checking if any seat changed, and repeat the process if needed.
    if ferry != original:
        part1(ferry)  
    
    # Counting the number of occupied seats if no seats changed state, and returning an int value.
    occupied = 0
    for row in ferry:
        occupied += row.count("#")
    return occupied


def part2(ferry):
    original2 = copy.deepcopy(ferry)
    for row_number, row in enumerate(ferry):
        for seat_number, seat in enumerate(row):
            if seat == ".":
                pass
            else:
                count = 0 # this will be used to create the "line of sight"
                aux = 0 # this will count occupied seats that the person sees from a seat.
                blocked_sight = {"up": False,
                    "down": False,
                    "left": False,
                    "right": False,
                    "up_left": False,
                    "up_right": False,
                    "down_left": False,
                    "down_right": False,} # This guy is used to know if a direction has already seen a seat.

                while  (
                        (row_number-count) >= 0 or
                        (row_number+count) < len(row) or
                        (seat_number-count) >= 0 or
                        (seat_number+count) < len(original2)
                        ):

                    count += 1
                    # Checking if we're on the first row. If we're on it, we never check seats above.
                    if (row_number - count) >= 0:

                        # We allways check the seats directly above current seat.
                        if blocked_sight["up"] == False:
                            if original2[row_number-count][seat_number] == '.':
                                pass
                            else:
                                aux += original2[row_number-count][seat_number].count("#")
                                blocked_sight["up"] = True

                        # Checking if we're on the first seat AND on the first row.
                        # If we're on it, we never check the seat to the left and above it.
                        if (seat_number - count) >= 0 and blocked_sight["up_left"] == False:
                            # Checking the seats on the left and above (diagonal)
                            if original2[row_number-count][seat_number-count] == '.':
                                pass
                            else:
                                aux += original2[row_number-count][seat_number-count].count("#")
                                blocked_sight["up_left"] = True
                        # Checking if we're on the last seat AND on the first row.
                        # If we're on it, we never check the seat to the right and above it.
                        if (seat_number + count) < len(row) and blocked_sight["up_right"] == False:
                            # If we're not on the last seat of the first row, we check the seat above to the right (diagonal).
                            if original2[row_number-count][seat_number+count] == '.':
                                pass
                            else:
                                aux += original2[row_number-count][seat_number+count].count("#")
                                blocked_sight["up_right"] = True

                    # Checking if on the first seat of any row.
                    if (seat_number - count) >= 0 and blocked_sight["left"] == False:
                        # Checking the seats in the same row but before the current seat.
                        if original2[row_number][seat_number-count] == '.':
                            pass
                        else:
                            aux += original2[row_number][seat_number-count].count("#")
                            blocked_sight["left"] = True
                    # Checking if on the last seat of any row.
                    if (seat_number + count) < len(row) and blocked_sight["right"] == False:
                        # Checking the seats in the same row but after the current seat.
                        if original2[row_number][seat_number+count] == '.':
                            pass
                        else:
                            aux += original2[row_number][seat_number+count].count("#")
                            blocked_sight["right"] = True
                    
                    # Checking if we're on the last row. If we're on it, we never check seats below.
                    if (row_number + count) < len(original2):

                        # We allways check the seat directly below the current seat.
                        if blocked_sight["down"] == False:
                            if original2[row_number+count][seat_number] == '.':
                                pass
                            else:
                                aux += original2[row_number+count][seat_number].count("#")
                                blocked_sight["down"] = True

                        # Checking if on the first seat AND on the last row.
                        if (seat_number - count) >= 0 and blocked_sight["down_left"] == False:
                            # Checking the seats below and to the left (diagonal)
                            if original2[row_number+count][seat_number-count] == '.':
                                pass
                            else:
                                aux += original2[row_number+count][seat_number-count].count("#")
                                blocked_sight["down_left"] = True
                        # Checking if on the last seat AND on the last row.
                        if (seat_number + count) < len(row) and blocked_sight["down_right"] == False:
                            # Checking the seats below and to the right (diagonal)
                            if original2[row_number+count][seat_number+count] == '.':
                                pass
                            else:
                                aux += original2[row_number+count][seat_number+count].count("#")
                                blocked_sight["down_right"] = True
            # Checking and changing the seat state, if needed.
            if seat == "L" and aux == 0:
                ferry[row_number][seat_number] = "#"
            elif seat == "#" and aux > 4:
                ferry[row_number][seat_number] = "L"
    # Checking if any seat changed, and repeat the process if needed.
    if ferry != original2:
        part2(ferry)
    
    # Counting the number of occupied seats if no seats changed state, and returning an int value.
    occupied = 0
    for row in ferry:
        occupied += row.count("#")
        #print(row)
    return occupied


if __name__ == "__main__":
    # By reading the file with: "f.read().splitlines()" we can treat the input like a matrix. As such,
    # input[r][c] returns the element in row "r" and column "c". By adding the map(list, file) we can  
    # change the values inside each element in the matrix without having to resort to string methods.
    if example:
        with open("Day 11/example_input", "r") as f:
            example_input = list(map(list, f.read().splitlines()))
        #print(part1(example_input))
        print(part2(example_input))
    if puzzle:
        with open("Day 11/puzzle_input", "r") as f:
            puzzle_input = list(map(list,f.read().splitlines()))
        print(part2(puzzle_input))
        