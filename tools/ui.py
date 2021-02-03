# Everything here runs the UI for the user

def isCustomer():
   x = input("Welcome to the fruit store. Are you a customer? (Y)") or "Y"
   if x.upper() == "Y" or x.upper() == "YES":
      return True

def printInstructions(userCommands):
   print("Commands:")

   # Print all avaliable commands (see 'userCommands' above)
   for command in userCommands:
      print(" " + command + " : " + userCommands[command])

def getInput(userCommands):
   # Get user input
   temp = input("\n > ")

   temp = temp.upper()

   # Error handling
   contains = False
   for command in userCommands:
      if temp == command:
         contains = True
   
   if not contains:
      return '0'
   
   return temp