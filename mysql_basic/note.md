**MySQL Structured Notes**

---

### **1. Connecting to MySQL Database**
```python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="anik",
    database="mydatabase"
)

mycursor = mydb.cursor()
```
*Establishes a connection with the MySQL database.*

---

### **2. Creating a Database**
```python
mycursor.execute("CREATE DATABASE mydatabase2")
```
*Creates a new database.*

---

### **3. Showing Databases**
```python
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
```
*Lists all available databases.*

---

### **4. Creating a Table**
```python
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
```
*Creates a table with an auto-increment primary key.*

---

### **5. Showing Tables**
```python
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
```
*Displays all tables in the database.*

---

### **6. Inserting Data into Table**
#### **Single Row Insert**
```python
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
```
*Inserts a single record into the table.*

#### **Multiple Row Insert**
```python
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652')
]
mycursor.executemany(sql, val)
mydb.commit()
```
*Inserts multiple records into the table.*

---

### **7. Fetching Data**
#### **Fetch All Rows**
```python
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
```
*Retrieves all rows from the table.*

#### **Fetch One Row**
```python
myresult = mycursor.fetchone()
print(myresult)
```
*Fetches only the first row.*

#### **Select Specific Columns**
```python
mycursor.execute("SELECT name, address FROM customers")
```
*Retrieves specific columns from the table.*

#### **Filtering with WHERE Clause**
```python
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Park Lane 38", )
mycursor.execute(sql, adr)
```
*Filters results based on a condition.*

#### **Using LIKE for Partial Match**
```python
sql = "SELECT * FROM customers WHERE address LIKE %s"
adr = ("%way%", )
mycursor.execute(sql, adr)
```
*Finds records that match a pattern.*

---

### **8. Sorting Data**
#### **Ascending Order**
```python
mycursor.execute("SELECT * FROM customers ORDER BY name")
```
*Sorts results in ascending order.*
#### **Descending Order**
```python
mycursor.execute("SELECT * FROM customers ORDER BY name DESC")
```
*Sorts results in descending order.*

---

### **9. Deleting Data**
#### **Delete Specific Record**
```python
sql = "DELETE FROM customers WHERE address = %s"
adr = ("Mountain 21", )
mycursor.execute(sql, adr)
mydb.commit()
```
*Deletes a record from the table.*

#### **Delete All Records**
```python
mycursor.execute("DELETE FROM customers")
mydb.commit()
```
*Removes all records from the table.*

#### **Delete Table**
```python
mycursor.execute("DROP TABLE customers")
```
*Deletes the entire table.*

---

### **10. Updating Data**
#### **Update a Record**
```python
sql = "UPDATE customers SET address = %s WHERE name = %s"
val = ("Valley 345", "John")
mycursor.execute(sql, val)
mydb.commit()
```
*Updates existing records.*

---

### **11. Limiting Results**
#### **Fetch Limited Rows**
```python
mycursor.execute("SELECT * FROM customers LIMIT 5")
```
*Limits the number of results returned.*

#### **Offset Results**
```python
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
```
*Skips specified rows before returning results.*

---

### **12. Joins**
#### **INNER JOIN (Matching Records in Both Tables)**
```python
sql = """
SELECT customers.name, orders.product
FROM customers
INNER JOIN orders ON customers.id = orders.customer_id
"""
mycursor.execute(sql)
```
*Retrieves matching records from both tables.*

#### **LEFT JOIN (All Records from Left Table + Matching from Right)**
```python
sql = """
SELECT customers.name, orders.product
FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
"""
mycursor.execute(sql)
```
*Returns all records from the left table and matching records from the right table.*

#### **RIGHT JOIN (All Records from Right Table + Matching from Left)**
```python
sql = """
SELECT customers.name, orders.product
FROM customers
RIGHT JOIN orders ON customers.id = orders.customer_id
"""
mycursor.execute(sql)
```
*Returns all records from the right table and matching records from the left table.*

---

This structured note covers key MySQL operations with Python. 🚀

