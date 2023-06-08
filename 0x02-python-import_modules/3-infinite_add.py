#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    result = 0

    if len(sys.argv) > 1:
        result = sum(int(i) for i in sys.argv[1:])
        print(result)
