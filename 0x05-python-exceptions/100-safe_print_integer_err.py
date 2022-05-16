#!/usr/bin/python3
import sys

text = "Exception: Unknown format code 'd' for object of type 'str'"


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        sys.stderr.write("{}\n".format(text))
        return False
    print()
