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
    spam.insert(-1, "and")

    i = 0
    try:  # Iterates through all but last two entries in list, adding commas and spaces.
        for i in range(len(spam) - 2):
            print(f"{spam[i]}, ", end="")
        print(f"{spam[-2]} {spam[-1]}")  # prints 'and' and last item in list
    except:  # If list is empty, except clause triggers.
        print("List is empty.")


spam = ["Alice", "Bob", 3.14159256, "apples", "oranges", 42, "cats", "dogs"]
# Outputs 'Alice, Bob, 3.14159256, apples, oranges, 42, cats, and dogs'
spam1 = []  # Outputs 'List is empty.'
spam2 = []  # Outputs 'List is empty.'
spam3 = ["Alice"]  # Outputs  'and Alice'
spam4 = [1]  # Outputs 'and 1'
eggs(spam)  # Calls function eggs and passes spam list as parameter.
