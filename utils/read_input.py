"""
This module provides utility functions for reading input from a file.
"""

def read_lines_from_file(file_name):
    """Reads in data from an input file as list of strings.

    Args:
        file_name (string): filename to read in.

    Returns:
        [string]: list from strings from file_name.
    """
    # fetch data as lines of text
    read_lines = []
    with open(file_name, "r", encoding="utf-8") as input_file:
        read_lines = input_file.readlines()

    return read_lines


def read_text_from_file(file_name):
    """Reads in data from an input file as a string.

    Args:
        file_name (string): filename to read in.

    Returns:
        string: string read from file.
    """
    # fetch data as lines of text
    read_string = ""
    with open(file_name, "r", encoding="utf-8") as input_file:
        read_string = input_file.read()

    return read_string
