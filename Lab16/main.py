import json

info = {
    "Name":"Bob",
    "age":20,
    "courses":["Math","English"]
}

json_string = json.dumps(info, indent=4)

print(json_string)

info = json.loads(json_string)

print(info)

filename = "example.json"

with open(filename, "w") as file:
    json.dump(info, file, indent=4)
print("nice")

with open("example.json", "r") as file:
    data = json.load(file)
print(data)
