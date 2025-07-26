from pathlib import Path
import sqlite3

connection = sqlite3.connect(Path.cwd()/'SQLite Basics'/'firstDB.db')

cursor = connection.cursor()

# Create a table
cursor.execute (
    """
    CREATE TABLE IF NOT EXISTS people (
        first_name TEXT,
        last_name TEXT,
        age INT
    );"""
)
# Insert a row of data
cursor.execute(
    """
    INSERT INTO people
        (first_name, last_name, age)
    VALUES
        ('John', 'Doe', 30),
        ('Jane', 'Smith', 25),
        ('Alice', 'Johnson', 28),
        ('Bob', 'Brown', 35);
    """
)
# Save (commit) the changes
connection.commit()
# Query the database
cursor.execute(
    """
    SELECT * FROM people;
    """
)
# Fetch the results
people = cursor.fetchall() #fetchall() retrieves all rows from the result set of a query
# Print the results
for person in people:
    print(person)
# Close the connection
connection.close()
# Note: The above code creates a database file named 'firstDB.db' in the current directory.