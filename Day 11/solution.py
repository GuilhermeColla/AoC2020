#! /usr/bin/env python3
import copy

example = 0
puzzle = 1

# If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
# If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
# Otherwise, the seat's state does not change.

def part1(ferry):
    original = copy.deepcopy(ferry) # .copy() needed because "original = ferry" doesn't create a new list.
    for row_number, row in enumerate(ferry):
        for seat_number, seat in enumerate(row):
            aux = 0 # counts occupied seats adjacent to the current seat.
            if seat == ".":
                pass
            else:
                # Need these conditions for the edges, because python returns a value for list[-1].
                if row_number > 0 and (0 < seat_number < (len(row)-1)):
                    aux += original[row_number-1][seat_number-1:seat_number+2].count("#")
                if row_number < (len(original)-1) and (0 < seat_number < (len(row)-1)):
                    aux += original[row_number+1][seat_number-1:seat_number+2].count("#")
                if seat_number > 0:
                    aux += original[row_number][seat_number-1].count("#")
                if seat_number < len(row)-1:
                    aux += original[row_number][seat_number+1].count("#")
                if seat_number == 0:
                    if row_number != len(original)-1:
                        aux += original[row_number+1][:seat_number+2].count("#")
                    if row_number != 0:
                        aux += original[row_number-1][:seat_number+2].count("#")
                if seat_number == len(row)-1:
                    if row_number != len(original)-1:
                        aux += original[row_number+1][seat_number-1:].count("#")
                    if row_number != 0:
                        aux += original[row_number-1][seat_number-1:].count("#")
                
                
                if seat == "L" and aux == 0:
                    ferry[row_number][seat_number] = "#"
                elif seat == "#" and aux > 3:
                    ferry[row_number][seat_number] = "L"
    if ferry != original:
        part1(ferry)   #todo: Count the occupied seats.  
    
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
        with open("Day 11/example_answer", "r") as f:
            example_answer = list(map(list, f.read().splitlines()))
        print(part1(example_input))
    if puzzle:
        with open("Day 11/puzzle_input", "r") as f:
            puzzle_input = list(map(list,f.read().splitlines()))
        print(part1(puzzle_input))
        