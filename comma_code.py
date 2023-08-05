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
    """
    Print list contents with commas between items and 'and' at penultimate position if
    length of list greater than 1. Otherwise, print zero index or inform user of index error.
    """
    try:
        if len(spam) == 1:
            print(spam[0])
        else:
            spam.insert(-1, "and")
            for bacon in spam[:-2]:
                print(f"{bacon}, ", end="")
            print(f"{spam[-2]} {spam[-1]}")
    except IndexError:
        print("List is empty.")


spam = ["Alice", "Bob", 3.14159256, "apples", "oranges", 42, "cats", "dogs"]
# Outputs 'Alice, Bob, 3.14159256, apples, oranges, 42, cats, and dogs'
spam1 = ["Bob", {"age": 42, "height": "6'9"}]
# Outputs 'Bob, and {'age': 42, 'height': "6'9"}'
spam2 = []
# Outputs 'List is empty.'
spam3 = ["Alice"]
# Outputs 'Alice'
spam4 = [1]
# Outputs '1'

spam_list = [spam, spam1, spam2, spam3, spam4]


def main():
    for item in spam_list:
        eggs(item)


if __name__ == "__main__":
    main()
