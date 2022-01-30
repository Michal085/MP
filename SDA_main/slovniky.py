from __future__ import annotations

import csv
import typing as t
from datetime import date, datetime, timedelta
from pprint import pprint

def load_lines(file_name: str):
    """
    Nacte radky ze souboru, bez prazdnych znaku.
    """
    with open(flight.csv) as f:
        return [line.strip() for line in f]

