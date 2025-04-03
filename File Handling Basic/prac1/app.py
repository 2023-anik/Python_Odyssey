#Create a new file "pracitice.txt". Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.
# 1. WAF that replace all occurrences of "Java" with "Python" in above file.
# 2. Search if the word "learning" exists in the file or not

# Method 1:
# with open("practice.txt", "r+t") as f:
#     data = f.read()
#     f.seek(0) # Move the cursor to the beginning of the file
#     f.write(data.replace("Java", "Python"))
#     f.seek(0)
#     if "learning" in f.read():
#         print("Word 'learning' exists in the file.")
#     else:
#         print("Word 'learning' does not exist in the file.")

# Method 2:
# f = open("practice.txt", "r+t")
# f.read().replace("Java", "Python")
# # f.close()
# # f = open("practice.txt", "r+t")
# f.seek(0) # Move the cursor to the beginning of the file
# if "learning" in f.read():
#     print("Word 'learning' exists in the file.")
# else:
#     print("Word 'learning' does not exist in the file.")
    

#Method 3:
def findWord(file, word):
    with open(file, "rt") as f:
        data = f.read()
        if word in data:
            return True
        else:
            return False

def lineNumOfFirstOccurence(file, word):
    lineNo = 0
    with open(file, "rt") as f:
        line = f.readline()
        while line:
            if word in line:
                lineNo += 1
                return lineNo
            line = f.readline()
            lineNo += 1
    return -1


with open("practice.txt", "rt") as f:
    data = f.read()
newData = data.replace("Java", "Python")
with open("practice.txt", "wt") as f:
    f.write(newData)
print(newData)
if findWord("practice.txt", "learning"):
    print("Word 'learning' exists in the file.")
else:
    print("Word 'learning' does not exist in the file.")

print(lineNumOfFirstOccurence("practice.txt", "learning"))
print(lineNumOfFirstOccurence("practice.txt", "Java"))