from pathlib import Path
from shutil import rmtree as rmdir

new_dir = Path.home() / "new_directory2"

paths = [
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.png",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_c" / "file2.txt",
    new_dir / "file1.txt",
    new_dir / "program1.py",
    new_dir / "program2.py",
]

for path in paths:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)

# move the file1.txt from scource to destication directory alse rename file1.txt to file1Moved.txt if wish
source = new_dir / "file1.txt"
destination = new_dir / "folder_a" / "file1Moved.txt"

# if not destination.exists():
#     source.replace(destination)

source.replace(destination)
print(source.exists())

# verify where the location of file1.txt
found = 0
for path in new_dir.rglob("file1.txt"):
    print(path)
    found = 1
if not found:
    print(f"No file is found")


##1
# # move or rename the folder_c to folder_d
# source = new_dir / "folder_c"
# destination = new_dir / "folder_d"
# # if not destination.exists():
# source.replace(destination)

# ##2
# source = new_dir / "folder_d"
# destination = new_dir / "folder_a" / "folder_e"
# # if not destination.exists():
# source.replace(destination)


# to delete a file, use the .unlink() method
file_path = new_dir / "program1.py"
file_path.unlink()
print(file_path.exists())
file_path.unlink(missing_ok=True) # missing_ok=True will not raise an error if the file does not exist


# to delete a directory, use the .rmdir() method
# directory_path = new_dir / "folder_a"
# #1st delete all files in the directory
# for path in directory_path.iterdir():
#     path.unlink()
# #2nd delete the directory
# directory_path.rmdir() # remove the directory
# print(directory_path.exists()) # check if the directory exists
# directory_path.rmdir(missing_ok=True) # missing_ok=True will not raise an error if the directory does not exist

# to delete a directory and all its contents, use the rmtree() method from the shutil module
rmdir(new_dir / "folder_a") # here rmdir is an alias for rmtree
print((new_dir / "folder_a").exists()) # check if the directory exists
rmdir(new_dir / "folder_a", ignore_errors=True) # ignore_errors=True will not raise an error if the directory does not exist
