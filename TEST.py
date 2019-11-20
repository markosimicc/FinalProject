import sqlite3
import time
import json
conn = sqlite3.connect('mock.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS testing(
id INTEGER PRIMARY KEY,name TEXT NOT NULL,
price TEXT NOT NULL,
quantity INTEGER
)""")
conn.commit()
# insertItem inserts an item into the mock database    
def insertItem(x,y,z):
    c=conn.cursor()
    c.execute('''INSERT INTO testing values(null,?,?,?)''',(x,y,z));
    conn.commit()
#returns the Item with specific ID 
def getItem(x):
    conn.row_factory = sqlite3.Row;
    c=conn.cursor();
    c.execute('SELECT * FROM testing where id = %i'%x);
    for row in c:
        #print(row[0],row[1],row[2],row[3]);
        temp = str(row['id']) + row['name'] + row['price'] + str(row['quantity']);
        return temp
# returns the quantity of the specific item     
def getQuantity(x):
    conn.row_factory = sqlite3.Row;
    c=conn.cursor()
    c.execute('SELECT quantity FROM testing WHERE id = %i'%x)
    for row in c:
        temp = row['quantity'];
    return temp
#returns the price of the given item ID
def getPrice(x):
    conn.row_factory = sqlite3.Row;
    c=conn.cursor()
    c.execute('SELECT price FROM testing WHERE id = %i'%x)
    for row in c:
        temp = row['price'];
    return temp
#increases the quantity of item id x by a factor of y 
def increaseQuantity(x,y):
    new = getQuantity(x) + y
    conn.row_factory = sqlite3.Row;
    c=conn.cursor()
    c.execute('UPDATE testing SET quantity = %d WHERE id = %i'%(new,x))
    c.execute('SELECT quantity FROM testing WHERE id = %i'%x)
    conn.commit()
    for row in c:
        temp = row['quantity'];
    return temp
# decreases the quantity of the given item by ID x by a factor of y
def decreaseQuantity(x,y):
    new = getQuantity(x) - y
    conn.row_factory = sqlite3.Row;
    c=conn.cursor()
    c.execute('UPDATE testing SET quantity = %d WHERE id = %i'%(new,x))
    c.execute('SELECT quantity FROM testing WHERE id = %i'%x)
    conn.commit()
    for row in c:
        temp = row['quantity'];
    return temp
#Checks if the shelf is empty or not returning true if it is empty 
def isEMPTY(x):
    var = getQuantity(x);
    if var == 0:
        return True;
    else:
        return False;


    
    

    
