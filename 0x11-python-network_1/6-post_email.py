#!/usr/bin/python3
"""
A Script that takes in a URL and an email sends a POST request to that URL
with the email as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    des = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(des.text))
