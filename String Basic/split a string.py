sentence = "Python is versatile language."
words = sentence.split()
print(words) # Output: ['Python', 'is', 'versatile', 'language.']
for word in words:
    print(word)
# Output:
# Python
# is
# versatile
# language.


#.split() also strips newlines by default.
text = """Line 1
Line 2
Line 3"""
lines = text.split()
print(lines) # Output: ['Line', '1', 'Line', '2', 'Line', '3']

#.splitline() to preserve newlines
text = """Hello, world!
How are you doing?"""
lines = text.splitlines()
print(lines) # Output: ['Hello, world!', 'How are you doing?']


# To preserve newlines, you can split on '\n':
lines = text.split(sep='\n')
print(lines) # Output: ['Line 1', 'Line 2', 'Line 3']

# You can also split a string based on a specific character. For example, the following code snippet splits a string based on a comma (,):
s = "apple,banana,grapes"
fruits = s.split(sep=",")
print(fruits)  # Output: ['apple', 'banana', 'grapes']

listFruit = "Apple;)Orange;)Lemon;)Date"
fruits = listFruit.split(sep=";)")
print(fruits)  # Output: ['Apple', 'Orange', 'Lemon', 'Date']


# You can also split a string based on a specific character and limit the number of splits. For example, the following code snippet splits a string based on a comma (,) and limits the number of splits to 2:
s = "apple,banana,grapes,orange,kiwi"
fruits = s.split(sep=",", maxsplit=2)
print(fruits)  # Output: ['apple', 'banana', 'grapes,orange,kiwi']


log_time = "2025-01-15 08:45:23 INFO User logged in from IP 10.0.1.1"
date, time, log_level, message = log_time.split(maxsplit=3)
print(f"Date: {date}")
print(f"Time: {time}")
print(f"Log Level: {log_level}")
print(f"Message: {message}")
# Output:
# Date: 2025-01-15
# Time: 08:45:23
# Log Level: INFO
# Message: User logged in from IP 10.0.1.1


#Go BAckwards Through a String Using .rsplit()
path = "home/user/documents/file.txt"
directory, fileName = path.rsplit(sep="/", maxsplit=1)
print(f"Directory: {directory}")
print(f"File Name: {fileName}")
# Output:
# Directory: home/user/documents
# File Name: file.txt


#Exercise: extract errors from a log file
log_data = """2025-01-15 08:45:23 INFO User logged in
2025-01-15 09:15:42 ERROR Failed to connect to server
2025-01-15 10:01:05 WARNING Disk space running low
"""
log_lines = log_data.splitlines()
for line in log_lines:
    if "ERROR" in line:
        print(line)
    # if(line.find("ERROR") != -1):
    #     print(line)