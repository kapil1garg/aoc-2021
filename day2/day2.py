"""
This module provides a solution for Advent of Code, Day 1: Sonar Sweep.
For more information, see: https://adventofcode.com/2021/day/2
"""
def get_sub_commands_from_input_file(file_name):
    """Reads in data from an input file, and converts strings to a list of numbers.

    Args:
        file_name ([string]): filename to read in.

    Returns:
        [[integer]]: list of integers read in from file_name.
    """
    # fetch data as lines of text
    lines = []
    with open(file_name, "rb") as input_file:
        lines = input_file.readlines()

    # parse strings into tuples of direction and value
    return [(curr_val.split()[0].strip().decode('UTF-8'), int(curr_val.split()[1].strip()))
    for curr_val in lines]

def determine_position_pt1(input_file):
    """Determines final position of submarine for Part 1 after executing commands from input_file.

    Args:
        input_file ([string]): filename to load data from.

    Returns:
        [integer]: final horizontal position multipled by depth position.
    """
    # get all commands
    sub_commands = get_sub_commands_from_input_file(input_file)

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


def determine_position_pt2(input_file):
    """Determines final position of submarine for Part 2 after executing commands from input_file.

    Args:
        input_file ([type]): [description]

    Returns:
        [type]: [description]
    """
    # get all commands
    sub_commands = get_sub_commands_from_input_file(input_file)

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

print(f"Part 1: {determine_position_pt1('input.txt')}")
print(f"Part 2: {determine_position_pt2('input.txt')}")
