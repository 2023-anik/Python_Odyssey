import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anik",
    database="mydatabase2"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255), fav INT AUTO_INCREMENT PRIMARY KEY)")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
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
#   ('Ben', 'Park Lane 38')
# ]

# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)

# mycursor.execute("CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(255), price INT)")

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# sql = "INSERT INTO products (product_name, price) VALUES (%s, %s)"
# val = [
#     ('Chocolate Heaven', 199),
#     ('Tasty Lemons', 111),
#     ('Vanilla Dreams', 97),
#     ('Caramel Bites', 101),
#     ('Strawberry Surprise', 101),
#     ('Coffee Deluxe', 111)
#     ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")

# sql = "CREATE TABLE new_table AS \
#     SELECT \
#         customers.name AS customer, \
#         customers.address AS address, \
#         products.product_name AS product \
#     FROM customers \
#     INNER JOIN products ON customers.fav = products.id"
# mycursor.execute(sql)

# sql = "CREATE TABLE new_table_left AS \
#     SELECT \
#         customers.name AS customer, \
#         customers.address AS address, \
#         products.product_name AS product \
#     FROM customers \
#     LEFT JOIN products ON customers.fav = products.id"
# mycursor.execute(sql)

# sql = "CREATE TABLE new_table_right AS \
#     SELECT \
#         customers.name AS customer, \
#         customers.address AS address, \
#         products.product_name AS product \
#     FROM customers \
#     RIGHT JOIN products ON customers.fav = products.id"
# mycursor.execute(sql)

# mycursor.execute("SELECT * FROM new_table_right")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)
