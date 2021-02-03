# Everything here runs the UI for the user AS A MANAGER

userCommands = {
   '?' : "Display these instructions", # Don't remove
   'V' : "View all products",
   'A' : "Add a product to cart",
   'C' : "View your cart",
   'Q' : "Quit"   # Don't remove
}

def handleInput(command, db):
   if command == 'V':
      products = db.collections("products").get()
      print(products.to_dict())