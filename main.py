from __future__ import annotations

import csv
import typing as t
from datetime import date, datetime, timedelta
from pprint import pprint
f = open('OpenData_Slovakia_Covid_AgTests_District (1).csv' , ' r ')
obsahSouboru = f.read()
def load_lines_v2(file_name, 'r' )  asfile:
    with open('OpenData_Slovakia_Covid_AgTests_District (1).csv', 'r') as file:
         lines = file.readlines()
         lst = [line.rstrip]('/n') for line in lines




