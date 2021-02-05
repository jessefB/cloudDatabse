# Everything here runs the UI for the user AS A CUSTOMER
from firebase_admin import firestore   # Needed for appending to arrays in the database


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
   # Here's the plan: ask for name, ask for product name, ask for quantity.
   # Get the user's name (this will find the cart)
   name = input("What is your name? ")
   query = db.collection("orders").where("customer", "==", name).get()

   if len(query) > 1:
      cart = pluralCart(query)
   elif len(query) == 1:
      cart = query[0].id
   else:
      cart = newCart(db, name)

   # Get the product
   product = input("What product do you want to add? ")
   quantity = input("How many %ss do you want? " % product.lower())
   quantity = int(quantity)

   # Get the product ID
   productID = db.collection("products").where("name", "==", product.capitalize()).get()[0].id

   # Add the item to the cart
   db.collection("orders").document(cart).update({"products" : firestore.ArrayUnion([productID])})

   # Add the quantity to the cart
   db.collection("orders").document(cart).update({"count" : firestore.ArrayUnion([quantity])})


# Create a new cart
def newCart(db, name):
   temp = {
      "customer" : name,
      "products" : [""],
      "count" : [""]
   }

   # Create a new document
   cart = db.collection("orders").document()

   # Add the info
   cart.set(temp)

   # Return the cart ID
   return cart


# Help determine what happens if there is more than one cart with the same customer
def pluralCart(query):
   # If there are more than one carts with a name
   print("Select which cart is yours:")

   for i, cart in enumerate(query):
      print(str(i) + ". %s" % cart.to_dict()["customer"] + " - Number of items: ", end='')
      print(str(len(cart.to_dict()["products"])))
   
   while True:
      cartNum = input("Cart number > ")

      # Error checking
      if cartNum.isdigit():
         return query[cartNum - 1]
      else:
         print("Invalid number. Try again.")


# Called with 'C'
def viewCart(db):
   # Get the user's name (this will find the cart)
   name = input("What is your name? ")
   query = db.collection("orders").where("customer", "==", name).get()

   # Make sure a cart exists
   if len(query) == 0:
      print("No cart for the name %s" % name)
      return

   # Make sure there is only one cart with the user's name
   if len(query) > 1:
      results = pluralCart(query)
   else:
      results = query[0]   # This just takes the first cart of the list

   # Print out the value of the cart
   printCart(results.to_dict(), db)

# Format the cart results
def printCart(results, db):
   total = 0

   # Header
   print("\nCustomer: %s" % results["customer"])

   # Table
   print("Name\t\t| Price\t| Quantity | Total")
   print("----------------+-------+----------+------")
   
   # Get each product by its ID from the cart array passed (as 'results')
   for index, item in enumerate(results["products"]):
      item = db.collection("products").document(item).get().to_dict()

      # Format name correctly
      if len(item["name"]) < 7:
         print(item["name"] + "\t\t| ", end='')
      else:
         print(item["name"] + "\t| ", end='')
      print(str(item["price"]) + "\t| ", end='')
      print(str(results["count"][index]) + "\t   | ", end='')
      lineTotal = results["count"][index] * item["price"]
      print(str(lineTotal))
      total += lineTotal

   print("\nTotal: %s" % "{:.2f}".format(total))
      


# Format for userCommands:
# Command : [Message, callback funtion]
userCommands = {
   'V' : ["View all products", viewProducts],
   'A' : ["Add a product to cart", addToCart],
   'C' : ["View your cart", viewCart]
}