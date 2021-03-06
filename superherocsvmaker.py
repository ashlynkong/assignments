import csv
import json

#read superheroes.json
with open('superheroes.json', 'r') as f:
	superheroes = json.load(f)

# loop through each member
members = superheroes['members']
for member in members:
	# print(member)

# save data for each member into a csv row
	with open('members.csv', 'w') as f:
		writer = csv.writer(f)
		header = ['name', 'age', 'secretIdentity', 'powers', 'squadName', 'homeTown', 'formed', 'secretBase', 'active']
		writer.writerow(header)

		for member in members:
			row = [
				member['name'],
				member['age'],
				member['secretIdentity'],
				member['powers'],
				superheroes['squadName'],
				superheroes['homeTown'],
				superheroes['formed'],
				superheroes['secretBase'],
				superheroes['active']
			]

			writer.writerow(row)