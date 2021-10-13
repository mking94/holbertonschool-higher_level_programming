#!/usr/bin/python3
""" Modul that save text to json file """
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representatio
    """
    with open(filename, 'w', encoding="UTF8") as f:
        json.dump(my_obj, f)
