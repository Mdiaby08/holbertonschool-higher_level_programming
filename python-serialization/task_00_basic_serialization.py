#!/usr/bin/env python3
"""
Basic serialization and deserialization using JSON.
"""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary to JSON and save it to a file."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file)
    except FileNotFoundError as e:
        # Invalid path → test expects OSError
        raise OSError("Invalid file path") from e
    except TypeError as e:
        # Non-serializable object → test expects TypeError
        raise TypeError("Data cannot be serialized") from e


def load_and_deserialize(filename):
    """Load JSON data from a file and return a dictionary."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
