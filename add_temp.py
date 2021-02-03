import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

proName = input("Product name: ")
quantity = input("Quantity: ")
price = input("Price: ")
isParent = input("isParent: ")

writeDict = {
   "name" : proName,
   "price" : float(price),
   "quantity" : int(quantity),
   "isParent" : bool(isParent)
   }

db.collection("products").add(writeDict)

print("Successfully written")