#!/usr/bin/env python3
"""
Basic serialization and deserialization using pickle.
"""

import pickle


def serialize_and_save_to_file(data, filename):
    """Serialize data and save it to a file."""
    with open(filename, "wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """Load data from a file and deserialize it."""
    with open(filename, "rb") as file:
        return pickle.load(file)
