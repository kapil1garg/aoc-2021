"""
This module provides a solution for Advent of Code, Day 2: Dive!.
For more information, see: https://adventofcode.com/2021/day/2
"""
import sys
import os

sys.path.append("..")
import utils.read_input as read_input


def parse_input(input_lines):
    """Parses list of strings from input file into list of tuples of direction and value.

    Args:
        input_lines ([string]): list of strings to prase.

    Returns:
        [(integer, integer)]: list of tuples of direction and value
    """
    # parse strings into tuples of direction and value
    return [(curr_val.split()[0].strip(), int(curr_val.split()[1].strip()))
    for curr_val in input_lines]


def day2_pt1(input_file):
    """Determines final position of submarine for Part 1 after executing commands from input_file.

    Args:
        input_file ([string]): filename to load data from.

    Returns:
        [integer]: final horizontal position multipled by depth position.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    sub_commands = parse_input(inputs)

    # store current position values
    horizontal = 0
    depth = 0

    # increment position values based on commands
    for command, value in sub_commands:
        if command == "forward":
            horizontal += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value

    # return final position
    return horizontal * depth


def day2_pt2(input_file):
    """Determines final position of submarine for Part 2 after executing commands from input_file.

    Args:
        input_file ([type]): [description]

    Returns:
        [type]: [description]
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    sub_commands = parse_input(inputs)

    # store current position values
    aim = 0
    horizontal = 0
    depth = 0

    # increment position values based on commands
    for command, value in sub_commands:
        if command == "forward":
            horizontal += value
            depth = depth + (aim * value)
        elif command == "down":
            aim += value
        elif command == "up":
            aim -= value

    # return final position
    return horizontal * depth

if __name__ == "__main__":
    input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    print(f"Part 1: {day2_pt1(input_filepath)}")
    print(f"Part 2: {day2_pt2(input_filepath)}")
