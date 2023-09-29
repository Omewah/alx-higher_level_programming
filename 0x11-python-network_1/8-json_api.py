#!/usr/bin/python3
"""
A Script that takes in a letter and sends a POST request to
https://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        datasend = {'q': sys.argv[1]}
    else:
        datasend = {'q': ""}

    des = requests.post("http://0.0.0.0:5000/search_user", data=datasend)

    try:
        des_json = des.json()
        if des_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(des_json['id'], des_json['name']))
    except ValueError:
        print("Not a valid JSON")
