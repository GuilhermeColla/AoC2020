#! /usr/bin/env python3
import copy

example = 1
puzzle = 0

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
    aux = 0 # this will count occupied seats that the person sees from a seat.
    count = 0 # this will be used to create the "line of sight"
    for row_number, row in enumerate(ferry):
        for seat_number, seat in enumerate(row):
            if seat == ".":
                pass
            else:
                while  (
                        (row_number-count) >= 0 or
                        (row_number+count) < len(row) or
                        (seat_number-count) >= 0 or
                        (seat_number+count) < len(original2)
                        ):

                    count += 1

                    # Checking if we arrived at the top row
                    if (row_number - count) >= 0:
                        aux += original2[row_number-count][seat_number].count("#")
                        # Checking if we arrived at the leftmost seat
                        if (seat_number - count) >= 0:
                            aux += original2[row_number-count][seat_number-count].count("#")
                            aux += original2[row_number][seat_number-count].count("#")
                        # rightmost seat
                        if (seat_number + count) < len(row):
                            aux += original2[row_number-count][seat_number+count].count("#")
                            aux += original2[row_number][seat_number+count].count("#")
                    # bottom row
                    if (row_number + count) < len(original2):
                        aux += original2[row_number+count][seat_number].count("#")
                        # leftmost seat
                        if (seat_number - count) >= 0:
                            aux += original2[row_number+count][seat_number-count].count("#")
                        # rightmost seat
                        if (seat_number + count) < len(row):
                            aux += original2[row_number+count][seat_number+count].count("#")
            # Checking and changing the seat state, if needed.
            if seat == "L" and aux == 0:
                ferry[row_number][seat_number] = "#"
            elif seat == "#" and aux > 3:
                ferry[row_number][seat_number] = "L"
    # Checking if any seat changed, and repeat the process if needed.
    if ferry != original2:
        part2(ferry)
    
    # Counting the number of occupied seats if no seats changed state, and returning an int value.
    occupied = 0
    for row in ferry:
        occupied += row.count("#")
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
        print(part1(puzzle_input))
        