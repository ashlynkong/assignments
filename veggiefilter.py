#read veggies.csv into a variable called vegetables
import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# filter whitelist names

green_veggies = []
whitelist = ['green']
for row in rows:
    if row['color'] in whitelist:
        green_veggies.append(row)

print(json.dumps(green_veggies, indent=2))