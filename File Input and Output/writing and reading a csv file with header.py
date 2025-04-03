from pathlib import Path
import csv

peoples = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

file_path = Path.home() / "peoples.csv"

with file_path.open(mode="w", encoding="utf-8") as file:
    # csv.DictWriter(file, fieldnames=peoples[0].keys()).writeheader()
    # csv.DictWriter(file, fieldnames=peoples[0].keys()).writerows(peoples)

    # insted of the above two lines, we can use the below line
    
    writer = csv.DictWriter(file, fieldnames=peoples[0].keys())
    writer.writeheader()
    writer.writerows(peoples)
    

# Reading a csv file
with file_path.open(mode="r", encoding="utf-8") as file:
    # print(csv.DictReader(file).fieldnames)  # Output: ['name', 'age']
    for row in csv.DictReader(file):
        row["age"] = int(row["age"])
        print(row)
        # Output: {'name': 'Alice', 'age': 30}
        # Output: {'name': 'Bob', 'age': 25}
        # Output: {'name': 'Charlie', 'age': 35}