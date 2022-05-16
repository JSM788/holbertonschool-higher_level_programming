#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as text:
        sys.stderr.write("{}\n".format(text))
        return False
    print()
