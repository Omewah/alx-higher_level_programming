#!/usr/bin/python3
"""
A script that takes in a URL and sends a request to the URL
and displays the body of the response decoded in utf-8
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    des = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(des) as reply:
            html = reply.read()
            print("{}".format(html.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
