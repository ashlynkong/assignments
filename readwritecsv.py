import csv
from pprint import pprint

# # write a CSV file
# with open('testwrite.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['col1', 'col2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])
#     writer.writerow(['val1', 'val2'])

# # read from a CSV
# with open('testwrite.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)

# pprint(rows)

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# open a CSV file
with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color'])
	# loop through veggies
	for vegetable in vegetables:
		print(vegetable)

		name = vegetable['name']
		color = vegetable['color']
		row = [name, color]

		writer.writerow(row)

