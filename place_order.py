
#%%
import sqlite3
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

supplierId = input("Type Supplier ID")

cursor.execute('SELECT * from suppliers WHERE supplierId=?', (supplierId,))
row = cursor.fetchone()

if row is None:
  print("Supplier Doesn't Exist")
else:
  id = row[0]
  name = row[1]
  print ("Supplier ID: " + str(id))
  print ("Supplier Name: " + str(name))

conn.commit()
