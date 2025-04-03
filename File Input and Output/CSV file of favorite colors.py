from pathlib import Path
import csv

favorite_colors = [
    {"name":"Joe", "favorite_color":"blue"},
    {"name":"Alice", "favorite_color":"red"},
    {"name":"Bob", "favorite_color":"green"},
    {"name":"Charlie", "favorite_color":"yellow"},
    {"name":"Dave", "favorite_color":"purple"},
]

file_path = Path.home()/"favorite_colors.csv"
#1
# file = file_path.open(mode="w", encoding="utf-8")
# writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])

# writer.writeheader()
# writer.writerows(favorite_colors)
# file.close()

#2
with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "favorite_color"])
    writer.writeheader()
    writer.writerows(favorite_colors)

with file_path.open(mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)