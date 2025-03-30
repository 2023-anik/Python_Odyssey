import pathlib

# path = pathlib.Path("'File Input and Output'/hello.txt")
path = pathlib.Path(r"File Input and Output/hello.txt") # r is for raw string
print(path.exists()) #To check if the file exists
print(path.is_file()) #To check if it is a file
print(path.is_dir()) #To check if it is a directory
print(path.name) #To get the name of the file or a directory

home = pathlib.Path.home()
print(home) #To get the home directory

current = pathlib.Path.cwd()
print(current) #To get the current directory

# check a path absolute or relative
print(path.is_absolute())
print(home.is_absolute())
print(current.is_absolute())

#extend a relative path to an absolute path
print(path.absolute())

#To get the parent directory
print(path.parent)

# To get an iterable list of directories and filen in the file path
absolute_path = home / path
list_of_directories = list(absolute_path.parents)
print(list_of_directories)
# iterate in a for loop
for directory in list_of_directories:
    print(directory)

# To acces the root directory
print(absolute_path.root) #1
print(absolute_path.anchor) #2 .anchor is the same as root
print(type(absolute_path.root)) #3
print(type(absolute_path.anchor)) #4
print(type(path.root))
print(type(path.anchor))

# .stem is the name of the file without the extension
print(path.stem)
# .suffix is the extension of the file
print(path.suffix)


print(absolute_path.exists()) #To check if the file exists
print(path.exists())
print(path.absolute().exists()) #To check if the file exists
print(path.is_file()) #To check if it is a file
print(path.is_dir()) #To check if it is a directory