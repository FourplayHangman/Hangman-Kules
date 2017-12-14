#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project:    Hangman
File:       get_ui_strings.py
Author:     Korvin F. Ezüst

Created:    2017-11-24
IDE:        PyCharm Community Edition

Get strings from a language file when available.
The language file is a csv file, uses comma as separator
and all strings are in-between double quotation marks.
"""

import csv
import os

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2017., Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "1.0"
__email__ = "dev@korvin.eu"
__status__ = "Development"

# Number of rows in the file
# Not actual row count but indexes
# including "END_OF_FILE" which is index ROW_COUNT
ROW_COUNT = 24


def get_strings(filename, language):
    """
    Makes sure that in case of a problem with the language file
    the GUI falls back to English

    :param filename: the language file
    :type filename: str
    :param language: the language
    :type language: str
    :return: strings used for the GUI
    :rtype: tuple
    """
    strings = get_strings_from_file(filename, language)
    if strings is None:
        return (
            "File VARIABLE could not be opened",
            ("Argument unrecognized.\nUsage:\n     game.py\n     "
             "game.py -h\n     game.py --help"),
            "proverbs.txt",
            "File not found:\nVARIABLE",
            "File seems corrupted:\nVARIABLE",
            ("\n\nWelcome to Proverbial Hangman!\n\nWhile in game, "
             "type \"exit\" or \"quit\" to leave the game.\n\nPress Enter "
             "to continue"),
            "\n\nThanks for playing! Bye!\n\n",
            "Incorrect guesses:\nVARIABLE",
            "The proverb: VARIABLE",
            "Guess:",
            "That's not a valid character",
            "You already made this guess",
            "You already made this guess\nPenalty +1",
            "You escaped hanging!",
            "You got hanged!",
            "Hangman Proverb",
            "Error",
            "Input Error",
            "Game Over",
            "Proverb:",
            "Incorrect Guesses",
            "Type your guess here",
            "New Game",
            "Exit")
    else:
        return strings


def get_strings_from_file(filename, language):
    """
    Reads the strings used in-game matching the selected language
    from the lang.csv file.

    The first line of the file contains the list of languages.
    The following lines are the strings.
    Each new column is a translation of the first one.
    The last line contains "END_OF_FILE" which indicates to
    this function that there's no more strings to read.
    The columns are separated by a comma and every string is in-between
    double quotation marks.

    Formatting errors and missing lines will result in this function
    returning None

    :param filename: path to lang.cvs
    :type filename: str
    :param language: selected language
    :type language: str
    :return: strings used in-game or None
    :rtype: str | None
    """
    f = open(filename)
    reader = csv.reader(f)

    # Get the number of languages in the csv file
    row = 0  # initialize here just in case...
    for row in reader:
        break

    # Return to the beginning of the file
    f.seek(0)

    language_count = len(row)
    if language_count == 0:
        return None

    # Read all lines into a list until reaching "END_OF_FILE"
    content = list()
    real_row_count = 0  # initialize here just in case...
    for real_row_count, row in enumerate(reader):
        if "END_OF_FILE" not in row:
            if len(row) == language_count:
                content.append(row)
            else:
                f.close()
                return None
        else:
            f.close()

            break
    f.close()

    # Check if the read lines' number is correct
    if real_row_count != ROW_COUNT:
        return None

    # Check if the selected language exists
    if language not in content[0]:
        return None

    # Get the index of the column of the selected language
    language_index = 0  # initialize just in case...
    for language_index, item in enumerate(content[0]):
        if item == language:
            break

    # Return None if there's an empty row
    for row in content:
        if len(row) == 0:
            return None

    # Get strings from the content list using the index from the previous loop
    strings = list()

    def replace_newline(s):
        """
        Replace the newline characters interpreted here as "\\n"
        with proper newline characters

        :param s: a string with wrong newline characters, if any
        :type s: str
        :return: a string with proper newline characters, if any
        :rtype: str
        """
        return s.replace("\\n", "\n")

    for i, row in enumerate(content):
        if i > 0:
            strings.append(replace_newline(row[language_index]))

    return strings


def get_language_list(filename):
    """
    Get the language list from the csv file

    :param filename: path to lang.csv
    :type filename: str
    :return: language list
    :rtype: list
    """
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            return list(row)


if __name__ == "__main__":
    language_file = os.path.join("../", "resources", "lang.csv")

    strings_from_file = get_strings_from_file(language_file, "magyar")
    print(strings_from_file)
