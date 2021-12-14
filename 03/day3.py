"""
This module provides a solution for Advent of Code, Day 3: Binary Diagnostic.
For more information, see: https://adventofcode.com/2021/day/3
"""
import sys
import os

sys.path.append("..")
import utils.read_input as read_input

def parse_input(input_lines):
    """Parses list of strings from input file into strings of binary numbers.

    Args:
        input_lines ([string]): list of strings to prase.

    Returns:
        [string]: list of binary numbers as strings.
    """
    # parse input into strings of binary numbers
    return [x.strip() for x in input_lines]


def day3_pt1(input_file):
    """Determines final position of submarine for Part 1 after executing commands from input_file.

    Args:
        input_file ([string]): filename to load data from.

    Returns:
        [integer]: final horizontal position multipled by depth position.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # parse input
    power_consumption_bin = parse_input(inputs)

    # get most common bit
    most_common_bits = []
    least_common_bits = []

    for bit_index in range(0, len(power_consumption_bin[0])):
        num_zero = 0
        num_one = 0

        for row in power_consumption_bin:
            if row[bit_index] == "0":
                num_zero += 1
            else:
                num_one += 1

        if num_zero > num_one:
            most_common_bits.append("0")
            least_common_bits.append("1")
        else:
            most_common_bits.append("1")
            least_common_bits.append("0")

    gamma_rate_str = ''.join(most_common_bits)
    epsilon_rate_str = ''.join(least_common_bits)

    return int(gamma_rate_str, base=2) *  int(epsilon_rate_str, base=2)


def day3_pt2(input_file):
    """Determines final position of submarine for Part 1 after executing commands from input_file.

    Args:
        input_file ([string]): filename to load data from.

    Returns:
        [integer]: final horizontal position multipled by depth position.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # parse input
    power_consumption_bin = parse_input(inputs)

    # get most common bit
    oxygen_rating = ""
    curr_list = list(power_consumption_bin)
    for bit_index in range(0, len(power_consumption_bin[0])):
        num_zero = 0
        num_one = 0
        curr_bit = None

        # edge case: only 1 row left
        if len(curr_list) == 1:
            oxygen_rating = curr_list[0]
            break

        for row in curr_list:
            if row[bit_index] == "0":
                num_zero += 1
            else:
                num_one += 1

        if num_zero > num_one:
            curr_bit = "0"
        elif num_one > num_zero:
            curr_bit = "1"
        else:
            curr_bit = "1"

        # filter the input based on the bit_index bit = curr_bit
        curr_list = [x  for x in curr_list if x[bit_index] == curr_bit]

    if oxygen_rating == "":
        oxygen_rating = curr_list[0]

    # get least common bit
    co2_rating = ""
    curr_list = list(power_consumption_bin)
    for bit_index in range(0, len(power_consumption_bin[0])):
        num_zero = 0
        num_one = 0
        curr_bit = None

        # edge case: only 1 row left
        if len(curr_list) == 1:
            co2_rating = curr_list[0]
            break

        for row in curr_list:
            if row[bit_index] == "0":
                num_zero += 1
            else:
                num_one += 1

        if num_zero > num_one:
            curr_bit = "1"
        elif num_one > num_zero:
            curr_bit = "0"
        else:
            curr_bit = "0"

        # filter the input based on the bit_index bit = curr_bit
        curr_list = [x  for x in curr_list if x[bit_index] == curr_bit]

    if co2_rating == "":
        co2_rating = curr_list[0]


    return int(oxygen_rating, base=2) *  int(co2_rating, base=2)


input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
print(f"Part 1: {day3_pt1(input_filepath)}")
print(f"Part 2: {day3_pt2(input_filepath)}")
