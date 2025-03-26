import pathlib

# path = pathlib.Path("'File Input and Output'/hello.txt")
path = pathlib.Path(r"File Input and Output/hello.txt") # r is for raw string
print(path.exists()) #To check if the file exists
print(path.is_file()) #To check if it is a file
print(path.is_dir()) #To check if it is a directory
print(path.name) #To get the name of the file

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