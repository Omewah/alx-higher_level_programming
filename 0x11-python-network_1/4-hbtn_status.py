#!/usr/bin/python3
"""A Script that fetches https://intranet.htbtn.io/status"""

import requests


if __name__ == "__main__":
    des = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(des.text)))
    print("\t- content: {}".format(des.text))
