#!/usr/bin/env python3
"""
Serialize and deserialize Python dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    try:
        # Create root element
        root = ET.Element("data")

        # Add dictionary items as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Write XML to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    try:
        # Parse XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct dictionary
        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except Exception:
        return None
