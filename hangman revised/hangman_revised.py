import os
import random
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import get_ui_strings

__author__ = "Korvin F. Ezüst"
__copyright__ = "Copyright (c) 2017., Korvin F. Ezüst"
__license__ = "Apache 2.0"
__version__ = "1.1"
__email__ = "dev@korvin.eu"
__status__ = "Development"


# TODO: test on Windows


def get_UMD_word(filename):
    """
    This function reads a random line from a given file.
    :param filename: absolute or relative path to a file
    :type filename: str
    :return: a UMD word
    :rtype: str
    """
    _ = 0  # initialize here
    with open(filename) as f:
        for _, line in enumerate(f):
            if "END_OF_FILE" in line:
                _ -= 1
                break

    # starts with index 1 because the first (index 0) line contains
    # the alphabet with all the letters used in UMD words in the file
    x = random.randint(1, _)
    with open(filename) as f:
        for _, line in enumerate(f):
            if _ == x:
                return line[:-1]


def get_alphabet(filename):
    """
    This function returns the alphabet, all the letters
    used in the file UMD words. The alphabet is
    the first line of the file.
    :param filename: the UMD words file
    :type filename: str
    :return: uppercase alphabet
    :rtype: str
    """
    with open(filename) as f:
        return f.readline().strip().upper()


def draw_hangman(x):
    """
    Creates a simple ASCII art of a hangman step by step from 0 to 10,
    then returns it as a string.
    :param x: current step
    :type x: int
    :return: simple ASCII art
    :rtype: str
    """
    if x == 0:
        img = "\n"
        img += " " + "—" * 15 + "\n"
        img += "   |" + " " * 9 + "|\n"
        img += "   |\n" * 6
        img += " " + "—" * 8

        return img
        #imgplot = plt.imshow(mpimg.imread('turtle7.jpg'))
        #plt.show()
    elif x == 1:
        imgplot = plt.imshow(mpimg.imread('turtle6.jpg'))
        plt.show()
    elif x == 2:
        imgplot = plt.imshow(mpimg.imread('turtle5.jpg'))
        plt.show()
    elif x == 3:
        imgplot = plt.imshow(mpimg.imread('turtle4.jpg'))
        plt.show()
    elif x == 4:
        imgplot = plt.imshow(mpimg.imread('turtle3.jpg'))
        plt.show()
    elif x == 5:
        imgplot = plt.imshow(mpimg.imread('turtle2.jpg'))
        plt.show()
    else:
        imgplot = plt.imshow(mpimg.imread('turtle1.jpg'))
        plt.show()

   # return img


def incomplete_UMD_word(pvb, lst, abc):
    """
    Returns a string where the unknown letters are replaced with
    underscores.
    Assumes everything is uppercase.
    :param abc: the alphabet used in the UMD words file
    :type abc: str
    :param pvb: a UMD word
    :type pvb: str
    :param lst: known letters
    :type lst: list
    :return: UMD_word with underscores replacing unknown letters
    :rtype: str
    """
    ret = ""
    for c in pvb:
        if c in abc and c not in lst:
            ret += "_"
        else:
            ret += c

    return ret


def wrong_guesses_to_display(lst):
    """
    Make a string from a list
    :param lst: list of strings
    :type lst: list
    :return: a string
    :rtype: str
    """
    ret = ""
    for _ in lst:
        if len(_) == 1:
            if len(ret) > 0:
                ret += ", " + _
            else:
                ret += _
    return ret


def complete_UMD_word(pvb):
    """
    Checks if the UMD word is complete.
    Assumes the UMD word is converted to have underscores replacing
    unknown letters.
    Assumes everything is uppercase.
    :param pvb: a UMD word
    :type pvb: str
    :return: True | False
    :rtype: bool
    """
    if "_" not in pvb:
        return True
    return False


def letter_only(guess, abc):
    """
    Checks if the player's guess is a single ASCII letter only.
    :param abc: the alphabet used in the proverbs
    :type abc: str
    :param guess: the player's guess
    :type guess: str
    :return: True | False
    :rtype: bool
    """
    if len(guess) == 1 and guess.upper() in abc:
        return True
    return False


def used_letters(guess, pvb, lst):
    """
    Checks if the player's guess is in the UMD_word. Adds it to the
    list of used letters if it's not.
    Assumes everything is uppercase.
    :param guess: the player's guess, a single letter
    :type guess: str
    :param pvb: the UMD_word
    :type pvb: str
    :param lst: known letters
    :type lst: list
    :return: known letters updated and sorted
    :rtype: list
    """
    if guess not in pvb:
        lst.append(guess)

    return sorted(lst)


def in_UMD_word(guess, pvb):
    """
    Checks if the player's guess is in the UMD_word.
    Assumes everything is uppercase.
    :param guess: a single letter
    :type guess: str
    :param pvb: the UMD_word
    :type pvb: str
    :return: True | False
    :rtype: bool
    """
    if guess in pvb:
        return True
    return False


def already_guessed(guess, lst):
    """
    Checks if the player's guess was already made.
    Assumes everything is uppercase.
    :param guess: a single letter
    :type guess: str
    :param lst: the list of guesses
    :type lst: list
    :return: True | False
    :rtype: bool
    """
    if guess in lst:
        return True
    return False


def get_max_guess_number():
    """
    Returns the number of guesses the player has
    :return: max guess number
    :rtype: int
    """
    return 6


if __name__ == '__main__':
    # Wrong argument message
    message = "Argument unrecognized.\n" \
              "Usage:\n" \
              "     game.py\n" \
              "     game.py -h\n" \
              "     game.py --help"

    # Check arguments
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 2:
        print(message)
        sys.exit(2)
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(__doc__)
        sys.exit(2)
    else:
        print(message)
        sys.exit(2)

    language_file = os.path.join("resources", "lang.csv")
    language_list = get_ui_strings.get_language_list(language_file)

    # Set a string to clear the command line
    # Tested only on Linux
    cls = "\033[H\033[J"
    # Clear command line
    print(cls, end="")

    # Ask player to choose language
    for i, l in enumerate(language_list):
        print(f"    {i + 1}: {l}")

    selection = 0
    while selection < 1 or selection > len(language_list):
        selection = input("--> ")
        if selection == "exit" or selection == "quit":
            sys.exit(0)
        try:
            selection = int(selection)
        except ValueError:
            pass

    language = language_list[selection - 1]

    # Get the strings corresponding to selected language
    # used in-game from lang.csv
    string_list = get_ui_strings.get_strings(language_file, language)

    # File name and path of UMD_words file
    umd_file = string_list[1]
    umd_path = os.path.join("resources", umd_file)

    # Get UMD_word
    UMD_word = get_UMD_word(umd_path)
    # Get alphabet
    alphabet = get_alphabet(umd_path)

    # Welcome message
    print(cls, end="")
    print(string_list[4])
    input()

    # Bye message
    bye = string_list[5]
    # Uppercase UMD_word
    UMD_word = UMD_word.upper()
    # List of the letters guessed and not in the UMD_word
    non_matches = []
    # List of the letters guessed and in the UMD_word
    matches = []
    # The UMD_word with underscores replacing unknown letters
    incomplete = incomplete_UMD_word(UMD_word, matches, alphabet)

    message = ""

    # Continue asking for input until the hangman
    # or the game is finished
    while len(non_matches) < get_max_guess_number():
        print(cls, end="")

        print(draw_hangman(len(non_matches)))

        inc_guesses = wrong_guesses_to_display(sorted(non_matches))
        # Print list of incorrect guesses
        print(f"{string_list[6]}".replace("VARIABLE", f"{inc_guesses}"))
        print(f"{string_list[7]}".replace("VARIABLE", f"{incomplete}"))
        print(message)

        # Get player input
        g = None
        while g is None:
            # ask player for guess
            g = input(f"{string_list[8]}")
            if letter_only(g, alphabet) is False:
                if g == "exit" or g == "quit":
                    print(bye)
                    sys.exit(0)
                g = None
                # print invalid input message
                print(f"{string_list[9]}")
            else:
                g = g.upper()

        # Check guess
        if already_guessed(g, matches):
            # correct guess already given
            message = f"{string_list[10]}"
        elif already_guessed(g, non_matches):
            # incorrect guess already given
            message = f"{string_list[11]}"
            # append "penalty" to non_matches
            non_matches.append("+1")
        elif in_UMD_word(g, UMD_word):
            matches.append(g)
            message = ""
        else:
            non_matches.append(g)
            message = ""

        # recreate var incomplete with new data
        incomplete = incomplete_UMD_word(UMD_word, matches, alphabet)

        if complete_UMD_word(incomplete):
            print("\n")
            print(incomplete, "\n")
            # win message
            print(f"{string_list[12]}")
            print(bye)
            sys.exit(0)

    print(cls, end="")

    print(draw_hangman(len(non_matches)), "\n")
    print(UMD_word.upper(), "\n")
    # lose message
    print(f"{string_list[13]}")
    print("\033[1;31;47m Bye  \n")

    sys.exit(0)
