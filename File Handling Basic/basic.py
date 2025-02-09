#To create a file
f = open("create.txt", "xt") # x is for create

#To open a file
f = open("first.txt", "rt") # r is for read, t is for text mode
print(f.read()) #To read a file
f.close() #To close a file


#To write a file
f = open("first.txt", "wt") # w is for write, t is for text mode
f.write("Hello World")
f.close()

#To append a file
f = open("first.txt", "at") # a is for append, t is for text mode
f.write("\nHello Vuban")
f.close()