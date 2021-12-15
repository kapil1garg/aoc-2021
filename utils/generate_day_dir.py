"""
This module is used to generate template directories for each new day in Advent of Code.
"""
from pathlib import Path
import re
import argparse

def generate_file_template(puzzle_name, day_name, day_url):
    """Generates a string for a template file that is used for an advent of code puzzle.

    Args:
        puzzle_name (string): title of day's puzzle.
        day_name (string): name of day, such as day1.
        day_url (string): URL to advent of code website for current day.

    Returns:
        string: content for template python file for advent of code puzzle.
    """
    template_string = f"""
    \"\"\"
    This module provides a solution for Advent of Code, {puzzle_name}.
    For more information, see: {day_url}.
    \"\"\"

    import sys
    import os

    sys.path.append("..")
    import utils.read_input as read_input


    def parse_input(input_list):
        \"\"\"Parses list of strings from input file into <type>.

        Args:
            input_list (list of strings): inputs read in from file as list of strings.

        Returns:
            (type): <description>.
        \"\"\"
        return None


    def {day_name}_pt1(input_file):
        \"\"\"<description>

        Args:
            input_file (string): filename to load data from.

        Returns:
            (type): <description>.
        \"\"\"
        # get input from file
        inputs = read_input.read_lines_from_file(input_file)

        # get all commands
        parsed_input = parse_input(inputs)

        # TODO: solve puzzle
        return None


    def {day_name}_pt2(input_file):
        \"\"\"<description>

        Args:
            input_file (string): filename to load data from.

        Returns:
            (type): <description>.
        \"\"\"
        # get input from file
        inputs = read_input.read_lines_from_file(input_file)

        # get all commands
        parsed_input = parse_input(inputs)

        # TODO: solve puzzle
        return None


    if __name__ == "__main__":
        input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
        print(f"Part 1: {{{day_name}_pt1(input_filepath)}}")
        print(f"Part 2: {{{day_name}_pt2(input_filepath)}}")
    """
    # preprocessing before saving
    # remove leading space from each line
    # remove newline from start of file
    # add 1 newline to end of file
    return "\n".join([re.sub(r"^ {4}", "", x) for x in template_string.split("\n")])


def main(day_num, puzzle_name, puzzle_url):
    """Create directory with __init__.py, dayX.py template file, and input.txt.

    Args:
        day_num (int): number for current day.
        puzzle_name (string): name of day's puzzle.
        puzzle_url (string): url to day's puzzle.
    """
    # create directory
    new_dir_name = f'{day_num:02}'
    Path(f"./{new_dir_name}").mkdir(exist_ok=True)

    # create __init__.py for module file
    open(f"./{new_dir_name}/__init__.py", "w", encoding='utf-8').close()

    # create template file for code
    day_name = f"day{day_num}"
    with open(f"./{new_dir_name}/{day_name}.py", "w", encoding='utf-8') as template_python_file:
        file_content = generate_file_template(puzzle_name, day_name, puzzle_url).strip() + "\n"
        template_python_file.write(file_content)

    # create template input file
    open(f"./{new_dir_name}/input.txt", "w", encoding='utf-8').close()


if __name__ == "__main__":
    # create argument parser
    parser = argparse.ArgumentParser(
        description="Generates a template directory for a day in Advent of Code.")
    parser.add_argument("day_num", type=int, help="Number of day.")
    parser.add_argument("puzzle_name", type=str, help="Name of day's puzzle.")
    parser.add_argument("puzzle_url", type=str, help="Url to puzzle.")

    # parse args and call main
    args = parser.parse_args()
    main(args.day_num, args.puzzle_name, args.puzzle_url)
