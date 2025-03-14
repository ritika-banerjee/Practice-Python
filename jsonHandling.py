import json

# data = {
#     "name" : "Alice",
#     "age" : 20,
#     "city" : "Kolkata"
# }

# with open("data.json", "w") as f:
#     json.dump(data, f, indent=4)

with open('data.json', "r") as f:
    data = json.load(f)

print(data)