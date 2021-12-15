"""
This module provides a solution for Advent of Code, Day 7: The Treachery of Whales.
For more information, see: https://adventofcode.com/2021/day/7.
"""
from statistics import mean
from math import inf
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
    """Computes the minimum cost to align crabs on a single point.
    Cost function is linear with the shift each crab needs to make to the target position.

    Args:
        input_file (string): filename to load data from.

    Returns:
        (int): minimum cost to align all crabs.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # get min and max positions
    min_pos = min(parsed_input)
    max_pos = max(parsed_input)

    # compute cost for each position that crabs can be aligned to
    min_cost = inf
    for target_pos in range(min_pos, max_pos + 1):
        # cost is linear shift from current position to target position
        curr_cost = sum(map(lambda x: abs(x - target_pos), parsed_input))

        # update cost
        min_cost = min(min_cost, curr_cost)

    return min_cost


def day7_pt2(input_file):
    """Computes the minimum cost to align crabs on a single point.
    Cost function is arithmetic sequence from 1 to shift amount with step size of 1.

    Args:
        input_file (string): filename to load data from.

    Returns:
        (int): minimum cost to align all crabs.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # get min and max positions
    min_pos = min(parsed_input)
    max_pos = max(parsed_input)

    # compute cost for each position that crabs can be aligned to
    min_cost = inf
    for target_pos in range(min_pos, max_pos + 1):
        # cost is arithmetic sequence from 1 to shift size
        curr_cost = int(sum(map(
            lambda x: mean([1, abs(x - target_pos)]) * abs(x - target_pos), parsed_input)))

        # update cost
        min_cost = min(min_cost, curr_cost)

    return min_cost


if __name__ == "__main__":
    input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    print(f"Part 1: {day7_pt1(input_filepath)}")
    print(f"Part 2: {day7_pt2(input_filepath)}")
