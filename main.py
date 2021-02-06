from tools import ui   # Handles all user stuff

# ------------- Heads up! You need your firebase credentials saved in a "creds.json" file in the same directory as this file -------------
# Database setup
import firebase_admin
from firebase_admin import credentials, firestore

# Credentials
try:
   cred = credentials.Certificate("creds.json")
   firebase_admin.initialize_app(cred)
except:
   print("No credentials found. See 'main.py' line 3.")
   quit()

db = firestore.client()

# Startup ------------------------------------------------------------
isCustomer = ui.isCustomer()  # Check if user is a customer or manager

# Get the correct UI tools
if isCustomer:
   from tools import customerUI as userUI
else:
   from tools import managerUI as userUI

# Loop ---------------------------------------------------------------
ui.printInstructions(userUI.userCommands)
while (True):

   # Get the command. Note that this has error checking built in. Any command returned is acceptable and uppercase
   command = ui.getInput(userUI.userCommands)

   # Loop defaults
   if command == '?':
      ui.printInstructions(userUI.userCommands)
      continue
   
   if command == 'Q':
      break

   # Call the appropriate function
   # Note: functions are stored as part of the userCommands dictionary
   userUI.userCommands[command][1](db)   # 1 is hard coded in because the function object is in slot 2 (starts at 0, remember?)

