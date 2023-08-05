#!/usr/bin/env python3
# comma_code.py — An exercise in understanding lists.
# For more information, see README.md

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="logging.txt",
    format="%(asctime)s -  %(levelname)s -  %(message)s",
)
logging.disable(logging.CRITICAL)  # Note out to enable logging.


def eggs(spam):
    """Returns string of contents from list with commas between items and 'and' at penultimate position if
    length of list greater than 1. Otherwise, return zero index."""

    if len(spam) == 1:
        bacon = spam[0]
    else:
        spam_string = [str(bacon) for bacon in spam]
        bacon = f"{', '.join(spam_string[:-1])}, and {spam_string[-1]}"
    return bacon


spam_1 = ["Alice", "Bob", 3.14159256, "apples", "oranges", 42, "cats", "dogs"]
# Outputs 'Alice, Bob, 3.14159256, apples, oranges, 42, cats, and dogs'
spam_2 = ["Alice"]
# Outputs 'Alice'
spam_3 = []
# Outputs 'List is empty.'


def main():
    try:
        print(eggs(spam_1))
    except IndexError:
        print("List is empty")


if __name__ == "__main__":
    main()
