# Everything here runs the UI for the user AS A CUSTOMER



# Called with 'V'
def viewProducts(db):
   # Create querey
   products = db.collection("products").get()

   # Display the products
   print("Name\t\t| Price\t| Quantity")
   print("----------------+-------+---------")
   for product in products:
      product = product.to_dict()
      if len(product["name"]) < 7:
         print(product["name"] + "\t\t| ", end='')
      else:
         print(product["name"] + "\t| ", end='')
      print(str(product["price"]) + "\t| ", end='')
      print(str(product["quantity"]))

# Called with 'A'
def addToCart(db):
   print("In addToCart func.... pretty cool huh?")

# Called with 'C'
def viewCart(db):
   pass


# Format for userCommands:
# Command : [Message, callback funtion]
userCommands = {
   'V' : ["View all products", viewProducts],
   'A' : ["Add a product to cart", addToCart],
   'C' : ["View your cart", viewCart]
}