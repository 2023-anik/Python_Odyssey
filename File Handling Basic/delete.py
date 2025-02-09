# To delete a file, need to import os module and use os.remove() method.

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#remove a empty folder
import os
if os.path.exists("myfolder"):
    os.rmdir("myfolder")
else:
    print("The folder does not exist")

#remove a folder with files
import shutil  # Import shutil module
import os  # Import os module

folder = "test"  # Folder name

if os.path.exists(folder):  # Check if folder exists
    shutil.rmtree(folder)  # Remove the folder and its contents
    print(f"{folder} has been removed.")
else:
    print("The folder does not exist.")