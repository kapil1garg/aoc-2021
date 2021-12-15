"""
This module provides a solution for Advent of Code, Day 4: Giant Squid.
For more information, see: https://adventofcode.com/2021/day/4
"""
import sys
import os
from functools import reduce

sys.path.append("..")
import utils.read_input as read_input


class BingoBoard:
    """Board object for playing bingo.
    """
    def __init__(self, input_lines):
        """Constructor

        Args:
            input_lines ([strings]): list of strings (of numbers) to create the bingo board with.
        """
        self.board = self.create_board_from_input(input_lines)


    def create_board_from_input(self, input_list):
        """Creates a bingo board from an input list of strings.

        Args:
            input_list ([strings]): list of strings (of numbers) to create the bingo board with.

        Returns:
            [[int]]: matrix of ints that represents a bingo board.
        """
        return [[int(num) for num in row.strip().split(" ") if num != ""] for row in input_list]

    def has_board_won(self, drawn_number_set):
        """Checks if the board is a winner, given a set of drawn numbers.

        Args:
            drawn_number_set (Set): set of numbers that have been drawn.

        Returns:
            boolean: true if a row or column has all numbers in the drawn number set.
        """
        # check rows
        for row in self.board:
            # all numbers in the row should be in the drawn_number_set
            if len(set(row) - drawn_number_set) == 0:
                return True

        # check columns
        for col_index in range(len(self.board[0])):
            # create a placeholder for the current column
            col = [x[col_index] for x in self.board]

            # all numbers in the col should be in the drawn_number_set
            if len(set(col) - drawn_number_set) == 0:
                return True

        return False


    def compute_final_board_score(self, drawn_number_set):
        """Computes the score for a winning board by
        summing all numbers on the board that weren't drawn.

        Args:
            drawn_number_set (set): numbers that were drawn during the bingo game.

        Returns:
            int: total sum of all numbers that were not drawn during the game.
        """
        # combine all numbers into a single set
        all_num_set = set([val for row in self.board for val in row])

        # do a set diff to see what numbers are still in the board that are not in the drawn set
        set_diff = all_num_set - drawn_number_set

        # return sum of unmarked numbers
        return reduce(lambda x, y: x + y, set_diff)


def parse_inputs(input_list):
    """Parses inputs into list of drawn numbers and list of BingoBoard objects.

    Args:
        input_list ([string]): inputs read in from file as list of strings.

    Returns:
        [int]: list of numbers drawn during bingo game.
        [BingoBoard]: list of BingoBoard objects from parsed inputs.
    """
    drawn_numbers = []
    bingo_boards = []
    last_index = 0
    for curr_index, line in enumerate(input_list):
        # first line is drawn numbers
        if curr_index == 0:
            drawn_numbers = [int(num) for num in line.strip().split(",")]

        # second line is empty space
        if curr_index == 1:
            last_index = curr_index + 1

        # third line onwards is either part of a row or an empty line
        if curr_index > 1:
            # check if new line to parse out bingo board
            if line == "\n":
                bingo_boards.append(BingoBoard(input_list[last_index:curr_index]))
                last_index = curr_index + 1

            # edge case for last line
            if curr_index + 1 == len(input_list):
                bingo_boards.append(BingoBoard(input_list[last_index:curr_index + 1]))

    return drawn_numbers, bingo_boards

def day4_pt1(input_file):
    """Computes the score of a winning bingo board, given bingo boards and a drawing of numbers.
    Score is the sum of all numbers that were not drawn multipled by the last drawn number.

    Args:
        input_file (string): name of file containing drawn numbers and bingo boards.

    Returns:
        [integer]: total sum of all numbers that were not drawn during the game
            multiplied by last drawn number.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # parse inputs
    drawn_numbers, bingo_boards = parse_inputs(inputs)

    # stream numbers and check if any of the boards have won
    curr_num_set = set()
    for curr_drawn_num in drawn_numbers:
        # add number to set
        curr_num_set.add(curr_drawn_num)

        # check to see if any of the boards have won
        for board in bingo_boards:
            if board.has_board_won(curr_num_set):
                board_sum = board.compute_final_board_score(curr_num_set)
                return board_sum * curr_drawn_num

    return inputs


def day4_pt2(input_file):
    """Computes the score of losing bingo board, given bingo boards and a drawing of numbers.
    Score is the sum of all numbers that were not drawn multipled by the last drawn number.

    Args:
        input_file (string): name of file containing drawn numbers and bingo boards.

    Returns:
        [integer]: total sum of all numbers that were not drawn during the game
            multiplied by last drawn number for the last board to win.
    """
    # get input from file
    inputs = read_input.read_lines_from_file(input_file)

    # parse inputs
    drawn_numbers, bingo_boards = parse_inputs(inputs)

    # stream numbers and check if any of the boards have won
    curr_num_set = set()
    last_called_num = None
    completed_boards = []
    for curr_drawn_num in drawn_numbers:
        # add number to set
        curr_num_set.add(curr_drawn_num)

        # check to see if any of the boards have won
        for board_index, board in enumerate(bingo_boards):
            # if a board has won, remove it from
            if board.has_board_won(curr_num_set) and board_index not in completed_boards:
                completed_boards.append(board_index)

        # check if any boards remain
        if len(completed_boards) == len(bingo_boards):
            last_called_num = curr_drawn_num
            break

    # compute the score of the last winning board
    last_board = bingo_boards[completed_boards[-1]]
    last_board_score = last_board.compute_final_board_score(curr_num_set)
    return last_called_num * last_board_score


if __name__ == "__main__":
    input_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input.txt')
    print(f"Part 1: {day4_pt1(input_filepath)}")
    print(f"Part 2: {day4_pt2(input_filepath)}")
