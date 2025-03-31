from pathlib import Path
import csv

numbers = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

file_path = Path.home() / "numbers.csv"

#1
with file_path.open(mode="w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(numbers)
    

#2
numbers = []
with file_path.open(mode="r", encoding="utf-8") as file:
    #1
    # for line in file.readlines():
    #     int_row = [int(num) for num in line.split(sep=",")]
    #     numbers.append(int_row)
    
    #2
    reader = csv.reader(file)
    for row in reader:
        # print(row) # Output: ['1', '2', '3', '4', '5']
        int_row = [int(num) for num in row]
        numbers.append(int_row)
print(numbers)