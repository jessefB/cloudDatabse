# Everything here runs the UI for the user

def isCustomer():
   x = input("Welcome to the fruit store. Are you a customer? (Y)") or "Y"
   if x.upper() == "Y" or x.upper() == "YES":
      return True

def printInstructions(userCommands):
   print("Commands:")

   # Print help command
   print(" ? : Display these instructions")
   # Print all avaliable commands from userCommands
   for command in userCommands:
      print(" " + str(command) + " : " + str(userCommands[command][0])) # 0 is the slot in which the message is stored

   # Print quit command
   print(" Q : Quit")

def getInput(userCommands):
   # Get user input
   temp = input("\n > ")

   temp = temp.upper()

   # Error handling
   contains = False
   for command in userCommands:
      if temp == command:
         contains = True
   
   # Defaults for interacting
   if temp == 'Q' or temp == '?':
      contains = True
   
   if not contains:
      return '0'
   
   return temp