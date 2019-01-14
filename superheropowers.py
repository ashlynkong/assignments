import json

# read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

data = []

# get members
members = superheroes['members']

# loop through each member, get list of powers
for member in members:
	powers = member['powers']

# loop through the powers and print each one
	for power in powers:
		data.append(power)

unique_powers = set(data)
unique_powers_list = list(unique_powers)
print(unique_powers_list)