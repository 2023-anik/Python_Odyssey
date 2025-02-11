ecute("SELECT * FROM new_table_right")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)