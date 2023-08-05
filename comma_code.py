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

spam_1 = ["Alice", "Bob", 3.14159256, "apples", "oranges", 42, "cats", "dogs"]
spam_2 = ["Alice"]
spam_3 = []


def main():
    """Print results of calling eggs on arguments with exception for empty list."""
    try:
        print(eggs(spam_1))
        print(eggs(spam_2))
        print(eggs(spam_3))
    except IndexError:
        print("List is empty")
    # Outputs:
    # Alice, Bob, 3.14159256, apples, oranges, 42, cats, and dogs
    # Alice
    # List is empty.


def eggs(spam):
    """Takes in list and returns string of contents with commas between items and 'and'
    at penultimate position if length greater than 1. Otherwise, return zero index."""

    if len(spam) == 1:
        bacon = spam[0]
    else:
        spam_string = [str(bacon) for bacon in spam]
        bacon = f"{', '.join(spam_string[:-1])}, and {spam_string[-1]}"
    return bacon


if __name__ == "__main__":
    main()
