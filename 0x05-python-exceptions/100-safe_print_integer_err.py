#!/usr/bin/python3

def safe_print_integer_err(value):
    import sys

    try:
        print("{:d}".format(int(value)))
        return True
    except ValueError:
        print("Exception: ValueError occurred", file=sys.stderr)
        return False
    except Exception as exc:
        print("Exception:", exc, file=sys.stderr)
        return False
