#!/usr/bin/python3
"""A Script that takes in a URL sends a POST request to that URL"""

import requests
import sys


if __name__ == "__main__":
    des = requests.get(sys.argv[1])
    if des.status_code >= 400:
        print("Error code: {}".format(des.status_code))
    else:
        print("{}".format(des.text))
