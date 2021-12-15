"""
This module provides a solution for Advent of Code, Day 5: Hydrothermal Venture.
For more information, see: https://adventofcode.com/2021/day/5.
"""
from functools import reduce
import sys
import os

sys.path.append("..")
import utils.read_input as read_input


def parse_input(input_list):
    """Parses list of strings from input file into 2 tuples of (x, y) coords.

    Args:
        input_list (list of strings): inputs read in from file as list of strings.

    Returns:
        list of tuple of 2 tuples: list of tuple of 2 tuples where
            first is start (x, y) coord, and second is end (x, y) coord.
    """
    parsed_input = []
    for line in input_list:
        first_coord_str, second_coord_str = (coord.strip() for coord in line.split(" -> "))
        first_coord_tuple = tuple(int(coord) for coord in first_coord_str.split(","))
        second_coord_tuple = tuple(int(coord) for coord in second_coord_str.split(","))

        parsed_input.append((first_coord_tuple, second_coord_tuple))

    return parsed_input

def update_matrix_for_line(matrix, start_coord, end_coord, include_diagonal):
    """Updates a matrix by incrementing values on the line specified by coords.

    Args:
        matrix (list of list of int): matrix representing ocean floor.
        start_coord (tuple of int): tuple of int representing start x, y coords.
        end_coord (tuple of int): tuple of int representing end x, y coords.
        include_diagonal (boolean): whether diagonal lines should be considered.

    Returns:
        (list of list of int): updated matrix with values along line incremented by 1.
    """
    # special case: consider only horizontal or vertical lines for pt1
    is_vertical = start_coord[0] == end_coord[0]
    is_horizontal = start_coord[1] == end_coord[1]
    if not is_vertical and not is_horizontal and not include_diagonal:
        return matrix

    # store the direction in which to step x and y forward
    x_step = -1 if start_coord[0] > end_coord[0] else 1
    y_step = -1 if start_coord[1] > end_coord[1] else 1

    # update matrix along line
    curr_coord = start_coord
    while curr_coord[0] != end_coord[0] or curr_coord[1] != end_coord[1]:
        # update cell with the current coords
        matrix[curr_coord[1]][curr_coord[0]] += 1

        # check if loop should be updated
        new_x_coord = curr_coord[0]
        new_y_coord = curr_coord[1]

        if new_x_coord != end_coord[0]:
            new_x_coord +=  x_step

        if new_y_coord != end_coord[1]:
            new_y_coord +=  y_step

        curr_coord = (new_x_coord, new_y_coord)

    # add to endpoint since that isn't in the loop above
    matrix[curr_coord[1]][curr_coord[0]] += 1

    return matrix

def day5_pt1(input_file):
    """Determines the number of spots on the ocean floor where 2+ lines overlap.
    Only considers vertical or horizontal lines.

    Args:
        input_file (string): filename to load data from.

    Returns:
        (int): count of locations where 2+ lines overlap.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # create matrix to represent ocean floor
    max_x = reduce(max, map(lambda coord: max(coord[0][0], coord[1][0]), parsed_input))
    max_y = reduce(max, map(lambda coord: max(coord[0][1], coord[1][1]), parsed_input))

    matrix = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

    # loop over each pair of coordinants and increment appropriate places in matrix
    for curr_input in parsed_input:
        matrix = update_matrix_for_line(matrix, curr_input[0], curr_input[1], False)

    # count any cells where 2 or more lines overlap
    return sum([item >= 2 for row in matrix for item in row])


def day5_pt2(input_file):
    """Determines the number of spots on the ocean floor where 2+ lines overlap.
    Only considers vertical, horizontal, and 45 degree diagonal lines.

    Args:
        input_file (string): filename to load data from.

    Returns:
        (int): count of locations where 2+ lines overlap.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # create matrix to represent ocean floor
    max_x = reduce(max, map(lambda coord: max(coord[0][0], coord[1][0]), parsed_input))
    max_y = reduce(max, map(lambda coord: max(coord[0][1], coord[1][1]), parsed_input))

    matrix = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

    # loop over each pair of coordinants and increment appropriate places in matrix
    for curr_input in parsed_input:
        matrix = update_matrix_for_line(matrix, curr_input[0], curr_input[1], True)

    # count any cells where 2 or more lines overlap
    return sum([item >= 2 for row in matrix for item in row])


if __name__ == "__main__":
    input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    print(f"Part 1: {day5_pt1(input_filepath)}")
    print(f"Part 2: {day5_pt2(input_filepath)}")
