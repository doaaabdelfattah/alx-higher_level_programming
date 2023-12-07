#!/usr/bin/python3
''' add items from arguments '''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
# In summary, this code is a simple script that loads a list of items from
# a JSON file (if the file exists),
# extends the list with command-line arguments,
# and then saves the updated list back to the same JSON file.
# The use of try-except allows the script to handle the case where the
# JSON file doesn't exist by initializing the items list with an empty list.

# The code uses a try-except block to attempt
# to load a list of items from the JSON file
# using the load_from_json_file function.
# If the file is not found (FileNotFoundError), it catches the exception
# and sets items to an empty list.
try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, 'add_item.json')
