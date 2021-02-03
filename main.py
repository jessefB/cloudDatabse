from tools import ui   # Handles all user stuff

# ------------- Heads up! You need your firebase credentials saved in a "creds.json" file in the same directory as this file -------------
# Database setup
import firebase_admin
from firebase_admin import credentials, firestore

# Credentials
cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)

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
   # Get the command
   command = ui.getInput(userUI.userCommands)

   # Program defaults
   if command == '?':
      ui.printInstructions(userUI.userCommands)
   
   if command == 'Q':
      break

   # Pass off user input to the specific user type
   userUI.handleInput(command, db)