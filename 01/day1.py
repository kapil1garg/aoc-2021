"""
This module provides a solution for Advent of Code, Day 1: Sonar Sweep.
For more information, see: https://adventofcode.com/2021/day/1
"""
import sys
import os

sys.path.append("..")
import utils.read_input as read_input


def parse_inputs(input_list):
    """Parses list of strings from input file into list of integers.

    Args:
        input_list ([string]): inputs read in from file as list of strings.

    Returns:
        [[integer]]: list of integers parsed from input strings.
    """
    # parse strings into integers and return
    return [int(curr_val.strip()) for curr_val in input_list]


def get_adj_increasing_count(num_list):
    """Counts how many adjacent values are increasing (curr val > prev val).

    Args:
        num_list ([integer]): list of integers.

    Returns:
        [integer]: number of times value is increasing.
    """
    prev_val = None
    increasing_count = 0

    # iterate over each value
    for curr_val in num_list:
        # if no value assigned, then set curr_val to the current value
        if prev_val is None:
            prev_val = curr_val
            continue

        # check if the current value is higher than the previous
        if curr_val > prev_val:
            increasing_count += 1

        # swap values
        prev_val = curr_val

    return increasing_count


def day1_pt1(input_file):
    """Gets the number of rows where the value is increasing, given an input file of integers.

    Args:
        input_file ([string]): input filename.

    Returns:
        [integer]: number of times a subsequent row increases in value.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # parse inputs
    numbers = parse_inputs(inputs)

    # compute increasing count and return
    return get_adj_increasing_count(numbers)


def day2_pt2(input_file, window_size):
    """Gets the number of times a running window is increasing.

    Args:
        input_file ([string]): input filename.
        window_size ([integer]): size of rolling window.

    Returns:
        [integer]: number of times a subsequent row increases in value.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # parse inputs
    numbers = parse_inputs(inputs)

    # create a list of rolling windows of window_size with all values in the window summed
    # from: https://stackoverflow.com/a/12709934
    windows = [sum(numbers[i-(window_size-1):i+1])
               if i > (window_size-1) else sum(numbers[:i+1])
               for i in range(len(numbers))]

    # remove the first window_size values since those will not be part of a summed window
    windows = windows[window_size-1:]

    # get the number of times the value is increasing
    return get_adj_increasing_count(windows)


input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
print(day1_pt1(input_filepath))
print(day2_pt2(input_filepath, 3))
