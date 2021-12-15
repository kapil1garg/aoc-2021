"""
This module provides a solution for Advent of Code, Day 6: Lanternfish.
For more information, see: https://adventofcode.com/2021/day/6.
"""

import sys
import os

sys.path.append("..")
import utils.read_input as read_input


def parse_input(input_list):
    """Parses list of strings from input file into list of ints.

    Args:
        input_list (list of strings): inputs read in from file as list of strings.

    Returns:
        (list of int): ints parsed from input list.
    """
    parsed_input = input_list[0].split(",")
    return [int(x) for x in parsed_input]


def simulate_fish_population(input_fishes, n_days):
    """Counts the number of fish after n_days, given a list of fishes with timers as input.
    Uses a dict to store the counts, which is faster and much more memory efficient than a list.

    Args:
        input_fishes (list of int): list of fishes with their initial timers.
        n_days (int): number of days to simulate.

    Returns:
        (int): total number of fishes after n_days.
    """
    # store fishes as pairs of timers:counts in a dictionary
    fish_dict = {x: 0 for x in range(0, 9)}
    for curr_fish in input_fishes:
        fish_dict[curr_fish] += 1

    # loop over days
    for _ in range(n_days):
        # create a new dict to store updated fish timer counts
        new_fish_dict = {x: 0 for x in range(0, 9)}

        # shift timers for fishes based on their current timers
        for timer, count in fish_dict.items():
            # add new fishes for 0 and add a count for 6 to reset fish
            if timer == 0:
                new_fish_dict[8] += count
                new_fish_dict[6] += count
            # add count for all fishes by decrementing their timer by 1
            else:
                new_fish_dict[timer - 1] += count

        # update original dict with new one
        fish_dict = new_fish_dict

    # return count of total fish
    return sum(fish_dict.values())


def day6_pt1(input_file):
    """Simulates fish population over 80 days.

    Args:
        input_file (string): filename to load data from.

    Returns:
        (int): number of fishes after 80 days.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # run simulation
    return simulate_fish_population(parsed_input, 80)


def day6_pt2(input_file):
    """Simulates fish population over 256 days.

    Args:
        input_file (string): filename to load data from.

    Returns:
        (int): number of fishes after 256 days.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # get all commands
    parsed_input = parse_input(inputs)

    # run simulation
    return simulate_fish_population(parsed_input, 256)


input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
print(f"Part 1: {day6_pt1(input_filepath)}")
print(f"Part 2: {day6_pt2(input_filepath)}")
