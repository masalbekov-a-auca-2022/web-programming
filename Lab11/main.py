company = {
    "employees": [
        {"name": "A", "salary": 300, "position": "Senior"},
        {"name": "B", "salary": 350, "position": "Junior"},
    ]
}

company["employees"].append({"name": "C", "salary":200, "position": "Middle"})

for employee in company["employees"]:
    print(employee["name"])