from __future__ import annotations

import csv

import typing as t

from datetime import date, datetime, timedelta

from pprint import pprint


def load_lines(file_name: str):
    """
    Nacita riadky zo suboru, bez prazdnych znakov.
    """
    with open(flight.csv) as f:
        return [line.strip() for line in f]

