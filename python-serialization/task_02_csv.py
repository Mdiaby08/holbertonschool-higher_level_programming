#!/usr/bin/env python3
"""
Convert CSV data into JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        # Read CSV file
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = list(reader)

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except Exception:
        return False
