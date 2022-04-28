#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    text = len(sys.argv)
    if text == 1:
        print("0 arguments.")
    else:
        print(f"{text - 1} arguments:")
    for count in range(1, text):
        print(f"{count}:", sys.argv[count])
