#!/usr/bin/env python3
"""Module for serializing and deserializing a dictionary to and from XML."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
    except (OSError, ET.ParseError):
        pass


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result
    except (FileNotFoundError, ET.ParseError, OSError):
        return {}
