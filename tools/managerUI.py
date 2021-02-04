# Everything here runs the UI for the user AS A MANAGER



# Called with 'V'
def viewProducts(db):
   # Create querey
   products = db.collection("products").get()

   # Display the products
   for product in products:
      print(product.to_dict())

# Called with 'P'
def addProduct(db):
   # Get necessary product information
   productInfo = {
      "name" : input("Product name: "),
      "price" : float(input("Price: ")),
      "quantity" : int(input("Quantity: ")),
      "isParent" : False   # For now I won't deal with parent products
   }

   # Now write it to the database
   db.collection("products").add(productInfo)
   print("Successfully added " + productInfo["name"])


# Format for userCommands:
# Command : [Message, callback funtion]
userCommands = {
   'V' : ["View all products", viewProducts],
   'P' : ["Add a product", addProduct]
}