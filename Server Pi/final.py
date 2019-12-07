import sqlite3
import time
import json
"""
Author: Marko Simic
The following code is used to create a database with two linked tables
and all functionalities of the database
This code is used by the Server RPi to get and insert info
"""
#creates connection to database
conn = sqlite3.connect('project.db')
#sets cursor
c=conn.cursor()
#creates first table 
c.execute("""CREATE TABLE IF NOT EXISTS shelves(
shelfid INTEGER PRIMARY KEY,
location TEXT NOT NULL,
itemid INTEGER NOT NULL,
FOREIGN KEY(itemid) REFERENCES items(id))
""")
#commits the changes
conn.commit()
#creates sceond linked table
c.execute("""CREATE TABLE IF NOT EXISTS items(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price TEXT NOT NULL,
quantity INTEGER NOT NULL)
""")
#commits changes
conn.commit()
"""
insertItem is used to insert data into the table items
Inputs: string name, string price, int qunantity
Return Boolan on if opeartion worked or not
"""
def insertItem(name,price,quantity):
    try:
        c.execute('''INSERT INTO items values(null,?,?,?)''',(name,price,quantity));
        conn.commit()
        return True
    except:
        return False
"""
insertShelf is used to insert data into the table shelves
Inputs: int shelfid, string location, int itemid
Return Boolan on if opeartion worked or not
"""
def insertShelf(shelfid, location,itemid):
    try:
        c.execute('''INSERT INTO shelves values(?,?,?)''',(shelfid,location,itemid));
        conn.commit()
        return True
    except:
        return False
"""
gets quantity of item in the table items
Input: Int itemid
Return: int quantity
"""
def getQuantity(itemid):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT quantity FROM items WHERE id = %i'%itemid)
        for row in c:
            temp = row['quantity'];
        #print(temp)
        return temp
    except:
        return None
"""
gets Name of item in the table items
Input: int itemid
Return: String Name
"""
def getName(itemid):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT name FROM items WHERE id = %i'%itemid)
        for row in c:
            temp = row['name'];
        #print(temp)
        return temp
    except:
        return None
"""
gets Price of item in the table items
Input: int itemid
Return: String Price
"""
def getPrice(itemid):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT price FROM items WHERE id = %i'%itemid)
        for row in c:
            temp = row['price'];
        print(temp)
        return temp
    except:
        return None
"""
gets Name of item in the table items
Input: int itemid
Return: String Item
"""
def getItem(itemid):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor();
        c.execute('SELECT * FROM items where id = %i'%itemid);
        for row in c:
            #print(row[0],row[1],row[2],row[3]);
            temp = str(row['id']) + row['name'] + row['price'] + str(row['quantity']);
        return temp
    except:
        return None
"""
Increases Quantity of shelf qunatity in table items
Inputs: int itemdid, int amount
return boolean on whetehr operation was complete or not 
"""
def increaseQuantity(itemid,amount):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT quantity FROM items WHERE id = %i'%itemid)
        conn.commit()
        for row in c:
            temp = row['quantity'];
        new = temp + amount#calculate new qunatity of item
        c.execute('UPDATE items SET quantity = %d WHERE id = %i'%(new,itemid))
        #after update comit the changes
        conn.commit()
        return True
    except:
        return False
"""
Decreases Quantity of shelf qunatity in table items
Inputs: int itemdid, int amount
return boolean on whetehr operation was complete or not 
"""
def decreaseQuantity(itemid,amount):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT quantity FROM items WHERE id = %i'%itemid)
        conn.commit()
        for row in c:
            temp = row['quantity'];
        new = temp - amount#calculate the changes
        c.execute('UPDATE items SET quantity = %d WHERE id = %i'%(new,itemid))
        #after update commit the changes
        conn.commit()
        return True
    except:
        return False

