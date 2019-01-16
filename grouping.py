#read veggies.csv into a variable called vegetables
import csv
import json
from pprint import pprint

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)


#group vegetables by color

vegetables_by_color = {}
for vegetable in vegetables:
    color = vegetable['color']
    if color in vegetables_by_color:
        vegetables_by_color[color].append(vegetable)
    else:
        vegetables_by_color[color] = [vegetable]

# pprint(vegetables_by_color)

#output vegetables_by_color into JSON

with open('vegetables_by_color.json', 'w') as f:
	json.dump(vegetables_by_color, f)
