import sqlite3
import serial
import time

arduino = serial.Serial('/dev/ttyACM0',9600)
conn = sqlite3.connect('mydatabase.db')
c=conn.cursor()
c.execute('SELECT * FROM items')
while 1:
    x = arduino.readline()
    x = int (x)
    sq1 = 'UPDATE items SET quantity = %d WHERE id = 1' %x
    c.execute(sq1)
    conn.commit()
    
    print("done")

