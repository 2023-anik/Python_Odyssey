import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="anik"
# )

# # print(mydb)
# mycursor = mydb.cursor() #cursor is used to interact with the database

# # mycursor.execute("SHOW DATABASES") #execute() method is used to execute the sql query
# # for x in mycursor:
# #     print(x)

# # mycursor.execute("CREATE DATABASE mydatabase2") #create a new database

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anik",
    database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))") #create a new table in the database mydatabase

#Data types in MySQL: INT, VARCHAR, TEXT, DATE, etc.
#VARCHAR(255) means that the field will contain a string with a maximum length of 255 characters.

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")# create a new table with primary key
#id is the primary key and it will auto increment itself, increment by 1

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") #add a primary key to an existing table

# mycursor.execute("SHOW TABLES") #show all the tables in the database
# for x in mycursor:
#     print(x)

# mycursor.execute("SHOW COLUMNS FROM customers") #show all the columns in the table customers
# for x in mycursor:
#     print(x)

# info = "INSERT INTO customers (name, address) VALUES (%s, %s)" #insert data into the table customers
# val = ("John", "Highway 21")
# mycursor.execute(info, val)

# mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Michelle", "Blue Village"))
# mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Sandy", "Ocean blvd 2"))
# mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Betty", "Green Grass 1"))
# mycursor.execute("INSERT INTO customers (name, address) VALUES (%s, %s)", ("Richard", "Sky st 331"))

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" #insert multiple rows into the table customers
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val) #executemany() method is used to insert multiple rows into a table

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)" #insert one row into the table customers
# val = ("Vuban", "Dhaka")
# mycursor.execute(sql, val)

# Escaping means safely handling special characters in user input.
# Use placeholders (%s) to escape values automatically.
# Never concatenate user input directly into SQL queries

# mydb.commit() #commit() method is required to make the changes, otherwise no changes are made to the table

# print(mycursor.rowcount, "record inserted.") #rowcount returns the number of rows affected by the last executed query
# print("1 record inserted, ID:", mycursor.lastrowid) #lastrowid returns the id of the last inserted row


# mycursor.execute("SELECT * FROM customers") #select all records from the table customers
# myresult = mycursor.fetchall() #fetchall() method, which fetches all rows from the last executed statement
# for x in myresult:
#     print(x)

# mycursor.execute("SELECT name FROM customers") #select only the name columns
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor.execute("SELECT name, address FROM customers") #select only the name and address columns
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# mycursor.execute("SELECT * FROM customers") #fetch only one row, it will return the first row
# myresult = mycursor.fetchone()
# print(myresult)

# sql = "SELECT * FROM customers WHERE address = %s" #select records where the address is "Park Lane 38"
# adr = ("Park Lane 38", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers WHERE address LIKE %s" #select records where the address contains the word "way"
# adr = ("%way%", ) # % is a wildcard character, which means "any number of characters"
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers ORDER BY name" #sort the result alphabetically by name
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers ORDER BY name DESC" #sort the result reverse alphabetically by name
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "DELETE FROM customers WHERE address = 'Mountain 21'" #delete the record where the address is "Mountain 21"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# sql = "DELETE FROM customers WHERE address = %s" #delete the record where the address is "Mountain 21"
# adr = ("Mountain 21", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# sql = "DELETE FROM customers WHERE address = %s" #delete any record where the address contains the word "way"
# adr = ("%way%", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# sql = "DELETE FROM customers" #delete all records from the table customers
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# sql = "DROP TABLE customers" #delete the table customers
# mycursor.execute(sql)

# sql = "DROP TABLE IF EXISTS customers" #delete the table customers if it exists
# mycursor.execute(sql)

# sql = "UPDATE customers SET address = %s WHERE address = %s'" #update the record where the address is "Valley 345"
# val = ("Canyon 123", "Valley 345")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# sql = "UPDATE customers SET address = %s" #update all records, set the address to "Valley 345"
# val = ("Valley 345", )
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# sql = "UPDATE customers SET address = %s WHERE name = %s" #update the record where the name is "John"
# val = ("Valley 345", "John")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")

# sql = "SELECT * FROM customers LIMIT 5" #limit the result to only return 5 records
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers LIMIT 5 OFFSET 2" #start from position 2, and return 5 records
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# sql = "SELECT * FROM customers LIMIT 2, 5" #start from position 2, and return 5 records
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

