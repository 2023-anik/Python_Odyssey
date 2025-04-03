############ Wichout csv module ############
# from pathlib import Path
# daily_temperatures = [
#     [68, 65, 68, 70, 74, 72],
#     [67, 67, 70, 72, 72, 70],
#     [68, 70, 74, 76, 74, 73]
# ]

# file_path = Path.home() / "temperatures.csv"

# file = file_path.open(mode="w", encoding="utf-8")

# for temp_list in daily_temperatures:
#     file.write(str(temp_list[0]))
#     for temp in temp_list[1:]:
#         file.write(f", {temp}")
#     file.write('\n')

# file.close()
##############################



############ using csv module ############
from pathlib import Path
import csv

file_path = Path.home() / "temperatures.csv"
# # file = file_path.open(mode="w", encoding="utf-8") # [1]

# # writer = csv.writer(file) # is used to write data to a CSV file

daily_temperatures = [
    [68, 65, 68, 70, 74, 72],
    [67, 67, 70, 72, 72, 70],
    [68, 70, 74, 76, 74, 73]
]

# # [1]
# # for temp_list in daily_temperatures:
# #     csv.writer(file).writerow(temp_list)
# # file.close()

# # [2] using with statement, automatically close the file
with file_path.open(mode="w", encoding="utf-8") as file:
    # for temp_list in daily_temperatures:
    #     csv.writer(file).writerow(temp_list)
    csv.writer(file).writerows(daily_temperatures)


# Reading a csv file [1]
# daily_temperatures_int = []
# for row in csv.reader(file_path.open(mode="r", encoding="utf-8")):
#     print(row) # Output: ['68', '65', '68', '70', '74', '72']
#     int_row = [int(temp) for temp in row]
#     daily_temperatures_int.append(int_row)

# print(daily_temperatures_int) # Output: [[68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70], [68, 70, 74, 76, 74, 73]]

# Reading a csv file [2]
daily_temperatures_int = []
with file_path.open(mode="r", encoding="utf-8") as file:
    for row in csv.reader(file):
        print(row) # Output: ['68', '65', '68', '70', '74', '72']
        # Convert each row from string to int
        # and append to daily_temperatures_int
        int_row = [int(temp) for temp in row]
        daily_temperatures_int.append(int_row)
print(daily_temperatures_int)
# Output: [[68, 65, 68, 70, 74, 72], [67, 67, 70, 72, 72, 70], [68, 70, 74, 76, 74, 73]]