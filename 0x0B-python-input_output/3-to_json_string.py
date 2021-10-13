#!/usr/bin/python3
""" to_json_string library """
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object
        """
    return json.dumps(my_obj)
