# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk
from tkinter import Button, Entry

def start_chatbot():
  ## Object of chatbase and display
  ## Welcome message
  print("Chatbot started")

  ##Create entry widget for user input
  user_input_entry = Entry(root, width=50)
  user_input_entry.pack()

  #Create buttons for various action
  login_button = Button(root, text="Login")
  login_button.pack()

  general_facts_button = Button(root, text="General Facts")
  general_facts_button.pack()

  business_contact_button = Button(root, text="Business Contact")
  business_contact_button.pack()





# Create the main GUI window
root = tk.Tk()
root.title("chatbot GUI")

# Create start button
start_button = Button(root, text="start", command=start_chatbot)
start_button.pack()

#run the GUI main loop
root.mainloop()
