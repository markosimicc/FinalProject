import sqlite3
import time
import json
conn = sqlite3.connect('project.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS shelves(
shelfid INTEGER PRIMARY KEY,
location TEXT NOT NULL,
itemid INTEGER NOT NULL,
FOREIGN KEY(itemid) REFERENCES items(id))
""")
conn.commit()
c.execute("""CREATE TABLE IF NOT EXISTS items(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price TEXT NOT NULL,
quantity INTEGER NOT NULL)
""")
conn.commit()
def insertItem(name,price,quantity):
    try:
        c.execute('''INSERT INTO items values(null,?,?,?)''',(name,price,quantity));
        conn.commit()
        return True
    except:
        return False
def insertShelf(shelfid, location,itemid):
    try:
        c.execute('''INSERT INTO shelves values(?,?,?)''',(shelfid,location,itemid));
        conn.commit()
        return True
    except:
        return False

def getQuantity(itemid):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT quantity FROM items WHERE id = %i'%itemid)
        for row in c:
            temp = row['quantity'];
        print(temp)
        return temp
    except:
        return None
def getName(itemid):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT name FROM items WHERE id = %i'%itemid)
        for row in c:
            temp = row['name'];
        print(temp)
        return temp
    except:
        return None
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
def increaseQuantity(itemid,amount):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT quantity FROM items WHERE id = %i'%itemid)
        conn.commit()
        for row in c:
            temp = row['quantity'];
        new = temp + amount
        c.execute('UPDATE items SET quantity = %d WHERE id = %i'%(new,itemid))
        conn.commit()
        return True
    except:
        return False
def decreaseQuantity(itemid,amount):
    try:
        conn.row_factory = sqlite3.Row;
        c=conn.cursor()
        c.execute('SELECT quantity FROM items WHERE id = %i'%itemid)
        conn.commit()
        for row in c:
            temp = row['quantity'];
        new = temp - amount
        c.execute('UPDATE items SET quantity = %d WHERE id = %i'%(new,itemid))
        conn.commit()
        return True
    except:
        return False

