#read() returns the entire content of the file as a single string
f = open("demfile.txt", "rt")
print(f.read())
f.close()

#read(n) returns the first n characters of the file
f = open("demfile.txt", "rt")
print(f.read(5))
f.close()

#readline() returns the content of the file line by line
f = open("demfile.txt", "rt")
line1 = f.readline()
line2 = f.readline()
print(line1, end="")
print(line2)
f.close()

#readlines() returns the content of the file as a list of lines
f = open("demfile.txt", "rt")
lines = f.readlines()
for line in lines:
    print(line, end="")
else:
    print("\n")
f.close()

#To read a file using "with" statement
with open("demfile.txt", "rt") as f:
    print(f.read())
    #No need to close the file as it is automatically closed