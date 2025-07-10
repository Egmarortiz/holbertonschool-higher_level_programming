#!/usr/bin/python3
"""serialization and deserialization using XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """serialization and deserialization using XML"""
    try:
        root = ET.Element('data')
        for key, value in dictionary.items():
            # create an element for each key
            child = ET.SubElement(root, key)
            child.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except (ET.ParseError, OSError, Exception):
        return False

def deserialize_from_xml(filename):
    """serialization and deserialization using XML"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}
        for child in root:
            result[child.tag] = _infer_type(child.text)
        return result
    except (ET.ParseError, OSError, Exception):
        return None

def _infer_type(text):
    """serialization and deserialization using XML"""
    if text is None:
        return None
    text = text.strip()
    low = text.lower()
    if low == 'true':
        return True
    if low == 'false':
        return False
    # integer?
    try:
        return int(text)
    except ValueError:
        pass
    # float?
    try:
        return float(text)
    except ValueError:
        pass
    # fallback
    return text
