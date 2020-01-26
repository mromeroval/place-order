# %%
#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Check if supplier exists
def checkSupplier(supplierId):
    cursor.execute(
        'SELECT supplierId from suppliers WHERE supplierId=?', (supplierId,))
    row = cursor.fetchone()
    if row is None:
        print("FAIL NO_SUPPLIER")
        conn.commit()
    else:
      supplierId = row[0]
      return supplierId


# Check if products of supplier exist
def checkSupplierProducts(supplierId, supplierProducts):
    productNames = []
    for productId in supplierProducts:
        cursor.execute('SELECT products.productName '
                      + 'FROM products '
                      + 'JOIN suppliers_products '
                      + 'ON products.productId = suppliers_products.productId '
                      + 'WHERE suppliers_products.supplierId = ? '
                      + 'AND  suppliers_products.productId = ?', (supplierId, productId,))
        row = cursor.fetchone()
        if row is None:
            print("FAIL NO_PRODUCT")
            break
        else:
            productNames.append(row[0])
            conn.commit()
    return productNames

# Get the order and split input in order to get suplier ID and array of products IDs
orderInput = input("place_order ")
orderArray = orderInput.split()
supplierid = orderArray[0]
products = orderArray[1].split(",")

supplierExist = checkSupplier(supplierid)
if supplierExist:
  productNames = checkSupplierProducts(supplierid, products)
  if productNames:
    print("OK ", productNames)

## TEST DATA ##
# c3e470 14fcbd,cc3c15
# q1w2e3 14fcbd,cc3c15
# q1w2e3 1q2w3e,2w3e4r,3e4r5t
# w2e3r4 4r5t6y,5t6y7u,6y7u8i
# e3r4t5 7u8i9o,8i9o0p,9i8u7y
