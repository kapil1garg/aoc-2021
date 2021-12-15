"""
This module provides a solution for Advent of Code, Day 7: The Treachery of Whales.
For more information, see: https://adventofcode.com/2021/day/7.
"""
from statistics import mean
import sys
import os

sys.path.append("..")
import utils.read_input as read_input


def parse_input(input_list):
    """Parses list of strings from input file into list of integers.

    Args:
        input_list (list of strings): inputs read in from file as list of strings.

    Returns:
        (list of int): list of integers.
    """
    return [int(x) for x in input_list[0].split(",")]


def day7_pt1(input_file):
    """<description>

    Args:
        input_file (string): filename to load data from.

    Returns:
        (type): <description>.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # get min and max positions
    min_pos = min(parsed_input)
    max_pos = max(parsed_input)

    min_cost = None
    for target_pos in range(min_pos, max_pos + 1):
        curr_cost = sum(map(lambda x: abs(x - target_pos), parsed_input))

        if min_cost == None or curr_cost < min_cost:
            min_cost = curr_cost

    return min_cost


def day7_pt2(input_file):
    """<description>

    Args:
        input_file (string): filename to load data from.

    Returns:
        (type): <description>.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

     # get all commands
    parsed_input = parse_input(inputs)

    # get min and max positions
    min_pos = min(parsed_input)
    max_pos = max(parsed_input)

    min_cost = None
    for target_pos in range(min_pos, max_pos + 1):
        curr_cost = sum(map(
            lambda x: mean([1, abs(x - target_pos)]) * abs(x - target_pos), parsed_input))
        curr_cost = int(curr_cost)

        if min_cost == None or curr_cost < min_cost:
            min_cost = curr_cost

    return min_cost


input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
print(f"Part 1: {day7_pt1(input_filepath)}")
print(f"Part 2: {day7_pt2(input_filepath)}")
