# read veggies.csv into a variable
import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

# print variable "vegetables"
# print(vegetables)

# save "vegetables" JSON as vegetables.json
with open('vegetables.json', 'w') as f:
    json.dump(vegetables, f, indent=2)
