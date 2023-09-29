#!/usr/bin/python3
"""
A Script that takes GitHub Credentials (username and password)
and uses GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    des = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    des_json = des.json()
    if des_json == {}:
        print("None")
    else:
        print("{}".format(des_json.get('id')))
