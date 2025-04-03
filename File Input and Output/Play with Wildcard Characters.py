from pathlib import Path

new_dir = (Path.home() / "new_directory" / "wildcards_Dir")
new_dir.mkdir(parents=True, exist_ok=True)  # Create the directory if it doesn't exist

paths = [
    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "file1.txt",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
    new_dir / "folder_c" / "file2.txt"
]

for path in paths:
    path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if they don't exist
    path.touch(exist_ok=True)  # Create the file if it doesn't exist


# List all paths that end in .py
list_of_dot_py = list(new_dir.glob("*.py"))
print(list_of_dot_py)
# using rglob to find all .py files in all subdirectories
list_of_dot_py_rglob = list(new_dir.rglob("*.py"))
print(list_of_dot_py_rglob)


# List any file path that matches the "*1*" pattern, means the path contains "1" with any number of characters before and after it.
List_of_1 = list(new_dir.glob("*1*"))
print(List_of_1)
# using rglob to find all files that match the "*1*" pattern in all subdirectories
List_of_1_rglob = list(new_dir.rglob("*1*"))
print(List_of_1_rglob)

List_of_1_astarisk_right_only = list(new_dir.glob("1*"))
print(List_of_1_astarisk_right_only)
# using rglob to find all files that match the "1*" pattern in all subdirectories
List_of_1_astarisk_right_only_rglob = list(new_dir.rglob("1*"))
print(List_of_1_astarisk_right_only_rglob)

# ? wildcard matches a single character
List_of_program_py = list(new_dir.glob("program?.py"))
print(List_of_program_py)
# using rglob to find all files that match the "program?.py" pattern in all subdirectories
List_of_program_py_rglob = list(new_dir.rglob("program?.py"))
print(List_of_program_py_rglob)


# multiple instances if ? in a single pattern
List_of_older_ = list(new_dir.glob("?older_?"))
print(List_of_older_)
#using rglob to find all files that match the "?older_?" pattern in all subdirectories
List_of_older_rglob = list(new_dir.rglob("?older_?"))
print(List_of_older_rglob)

# Combine the * and ? wildcards
List_of_combines1 = list(new_dir.glob("*1.??"))
print(List_of_combines1)
# using rglob to find all files that match the "*1.??" pattern in all subdirectories
List_of_combines1_rglob = list(new_dir.rglob("*1.??"))
print(List_of_combines1_rglob)
List_of_combines2 = list(new_dir.glob("*1.???"))
print(List_of_combines2)


#[] wildcard matches a single character in a set of characters
List_of_set = list(new_dir.glob("program[134].py"))
print(List_of_set)
# using rglob to find all files that match the "program[134].py" pattern in all subdirectories
List_of_set_rglob = list(new_dir.rglob("program[134].py"))
print(List_of_set_rglob)
