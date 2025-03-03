filename = "text.txt"
content = ("ONE\n"
           "TWO\n"
           "THREE")

with open(filename, "w") as f:
    f.write(content)

with open(filename, "r") as f:
    read_content = f.read()

print(read_content)

import csv

csv_filename = "text.csv"

data = [
    ["Name", "Salary", "Gender"],
    ["Alice", 75, "F"],
    ["John", 100, "M"],
    ["Stewart", 200, "M"]
]

with open(csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)
    print("nice")

with open(csv_filename, "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

add_text = "\nFOUR"

with open(filename, "a") as f:
    f.write(add_text)
print("nice")

with open(filename, "r") as f:
    content = f.read()
print(content)