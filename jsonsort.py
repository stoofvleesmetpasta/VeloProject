import json
f = open("velo.json", "r")
data = json.load(f)

for item in data:
    keys_to_remove = ["geometry", "Aanvulling", "District", "Huisnummer"]
    for key in keys_to_remove:
        item.pop(key, None)

sorted_data = json.dumps(data, indent=4, sort_keys=True)

with open('velo.json', 'w') as file:
    file.write(sorted_data)
