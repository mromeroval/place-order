#%%
#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Check if supplier exist
def checkSupplier(supplierId):
  cursor.execute('SELECT * from suppliers WHERE supplierId=?', (supplierId,))
  row = cursor.fetchone()
  if row is None:
    print("FAIL NO_SUPPLIER")
  else:
    id = row[0]
    name = row[1]
    print ("Supplier ID: " + str(id))
    print ("Supplier Name: " + str(name))
    conn.commit()

orderInput = input("place_order ")
# c3e470 14fcbd,cc3c15
# q1w2e3 14fcbd,cc3c15

orderArray = orderInput.split()
id = orderArray[0]
products = orderArray[1]
checkSupplier(id)
