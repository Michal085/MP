import csv
with open('Slovakia_Covid_AgTests.csv', newline='', encoding='utf-8') as f:
    tests = csv.reader(f)
    for test in tests:
        print(test)



