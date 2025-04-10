from pathlib import Path
import sqlite3

with sqlite3.connect(Path.cwd()/'SQLite Basics'/'firstDB.db') as connection:
    cursor = connection.cursor()

    # Create a table
    cursor.execute (
        """
        CREATE TABLE IF NOT EXISTS people2 (
            first_name TEXT,
            last_name TEXT,
            age INT
        );"""
    )
    # Insert a row of data
    cursor.execute(
        """
        INSERT INTO people2
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
        SELECT * FROM people2;
        """
    )
    # Fetch the results
    people = cursor.fetchall()
    # Print the results
    for person in people:
        print(person)