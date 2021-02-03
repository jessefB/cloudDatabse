# Everything here runs the UI for the user AS A MANAGER

userCommands = {
   '?' : "Display these instructions", # Don't remove
   'V' : "View all products",
   'A' : "Add a product to cart",
   'C' : "View your cart",
   'Q' : "Quit"   # Don't remove
}

def handleInput(command, db):
   # Dear future me. This is working. Returns all the products in the db. 4:15 2/3/21
   if command == 'V':
      products = db.collection("products").get()
      for pro in products:
         print(pro.to_dict())