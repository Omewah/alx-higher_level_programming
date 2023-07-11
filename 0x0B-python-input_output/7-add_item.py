#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
from pathlib import path
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

item = []
if path('add_item.json').exists():
    items = load_from_json_file('add_item.json')

for i in range(1, len(sys.argv)):
    item.append(str(sys.argv[i]))

save_to_json_file(items, 'add_item.json')
