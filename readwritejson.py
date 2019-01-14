import json
from pprint import pprint

# reading JSON

# with open('superheroes.json', 'r') as f:
#     data = json.load(f)

# pprint(data)

# writing a JSON file

rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('friends.json', 'w') as f:
    json.dump(rows, f, indent=2)