#!/usr/bin/python3
"""Function that appends a string at the end of a text/
file"""


def append_write(filename="", text=""):
    """Returns the number of characters added"""

    with open(filename, "w", encoding="utf-8") as f:
        write_data = f.write(text)
        write_data = f.write(text)
        return(write_data)
