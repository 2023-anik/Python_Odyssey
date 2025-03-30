from pathlib import Path

# Create a new directory
new_dir = Path.home() / "new_directory"
new_dir.mkdir(exist_ok=True) # exist_ok=True will not raise an error if the directory already exists
# Check if the directory was created
print(new_dir.exists())  # True if the directory was created successfully
# Check if it is a directory
print(new_dir.is_dir())  # True if it is a directory

# Create nested Directory
nested_dir = new_dir / "nested_directory1" / "nested_directory2"
nested_dir.mkdir(parents=True, exist_ok=True)  # parents=True will create all parent directories


# Create a new file
new_file = new_dir / "file3.txt"
new_file.touch(exist_ok=True)  # exist_ok=True will not raise an error if the file already exists
file_path = new_dir / "folder_c" / "file2.txt"
file_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if they don't exist
file_path.touch(exist_ok=True)  # exist_ok=True will not raise an error if the file already exists
# Check if the file was created
print(file_path.exists())  # True if the file was created successfully
# Check if it is a file
print(file_path.is_file())  # True if it is a file


for path in new_dir.iterdir():
    print(path)  # Print all files and directories in the new directory

# Convert a directory's all path in a list
list_of_paths = list(new_dir.iterdir())
# Print all files and directories in the new directory
print(list_of_paths)


#Iterate through all files in a directory by using glob
for path in new_dir.glob("*.txt"): # Use glob to find all .txt files
    print(path)  # Print all files and directories in the new directory

#Iterate through all files in a directory by using rglob


#convert  the path to a list of a directory
list_of_path = list(new_dir.glob("*.txt"))
print(list_of_path)  # Print all files and directories in the new directory


#Iterate through all files in a directory by using rglob
for path in new_dir.rglob("*.txt"): # Use rglob to find all .txt files in all subdirectories
    print(path)  # Print all files and directories in the new directory
#Iterate through all files in a directory by using rglob
#convert  the path to a list of a directory
list_of_path = list(new_dir.rglob("*.txt"))
print(list_of_path)  # Print all files and directories in the new directory
#Iterate through all files in a directory by using rglob



