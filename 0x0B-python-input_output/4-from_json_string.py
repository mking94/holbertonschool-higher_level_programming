#!/usr/bin/python3
""" Define module convert from JSON to Python data"""
import json


def from_json_string(my_str):
    """
    Return a python object represented by a JSON string
    """
    return json.loads(my_str)
