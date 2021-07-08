import mysql.connector
from tkinter import *


root = Tk()    
root.title("Loren's TK Database")
root.iconbitmap("E:/OC/pushcode/Python Resume files/icon.ico")

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Tr@n$1t10n",
    database = "testdb"
    )

# Create cursor    
c = mydb.cursor()
def submit():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "Tr@n$1t10n",
        database = "testdb"
        )

# Create cursor    
    c = mydb.cursor()

# Create Submit function
# def submit():
    # Actually submit to table
    c.execute("INSERT INTO addresses VALUES (:first_name, :last_name, :address, :city, :state, :zipcode)",
        {
            'first_name' : first_name.get(),
            'last_name' : last_name.get(),
            'address' : address.get(),
            'city' : city.get(),
            'state' : state.get(),
            'zipcode' :zipcode.get()
        })
    
    
    # Commit Changes
    mydb.commit()

# Close Connection
    mydb.close()

    # Clear the Text Boxes
    first_name.delete(0, END)
    last_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#c.execute(""" CREATE TABLE addresses (
#       first_name text,
#      last_name text,
#       address text,
#       city text,
#       state text,
#       zipcode integer
#       )""")

first_name = Entry(root, width=30)
first_name.grid(row=0, column=1, padx=20)

last_name = Entry(root, width=30)
last_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create Textbox Label

first_name_label = Label(root, text="First Name")
first_name_label.grid(row=0, column=0)

last_name_label = Label(root, text="Last Name")
last_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)



# my_cursor.execute("CREATE DATABASE KOHDB")

# my_cursor.execute("SHOW DATABASES")
# for db in my_cursor:
#    print(db[0])

# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(3), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")#
# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table[0])
    
# sqlstuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("Loren Stevenson", "loren8247@gmail.com", 38)
# my_cursor.execute(sqlstuff, record1)
# mydb.commit()
    # Commit Changes
mydb.commit()

# Close Connection
mydb.close()

root.mainloop()
