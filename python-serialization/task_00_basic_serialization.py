#!/usr/bin/python3
"""Basic encoding and decoding"""


import json


def serialize_and_save_to_file(data, filename):
    """Encoding data into file"""
    with open(filename, 'w', endcoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Decoding data into file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
