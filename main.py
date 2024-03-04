###PROPERTY OF
###SHABEG, JOSE, NATHAN, MARSELIS, RASHA


import tkinter as tk
from tkinter import Button, Entry, Label, messagebox, Toplevel
import sqlite3

#Connect to SQLlite Database
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create Users table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    UserID INTEGER PRIMARY KEY,
                    Email TEXT UNIQUE NOT NULL,
                    Password TEXT NOT NULL
                  )''')
conn.commit()


root = tk.Tk()
root.title("chatbot GUI")
###GUI SIZE
window_width = root.winfo_screenwidth() // 5  # 1/5 of screen width
window_height = root.winfo_screenheight() // 2  # Half of screen height
root.geometry(f"{window_width}x{window_height}")

#Connect to SQLlite Database



def on_click(event):
  if user_input_entry.get() == "Please ask any questions":
    user_input_entry.delete(0, tk.END)

def start_chatbot():
    ## Object of chatbase and display
    ## Welcome message
  print("Welcome! The Chatbot is ready for your questions")


##Login Button
def open_login_page():
  login_window = Toplevel(root)
  login_window.title("Login")
  ####Add widgets for login page (e.g., labels, entry fields, login button)
  login_window = Toplevel(root)
  login_window.title("Login")

  email_label = Label(login_window, text="Email:")
  email_label.grid(row=0, column=0, padx=10, pady=5)
  email_entry = Entry(login_window)
  email_entry.grid(row=0, column=1, padx=10, pady=5)

  password_label = Label(login_window, text="Password:")
  password_label.grid(row=1, column=0, padx=10, pady=5)
  password_entry = Entry(login_window, show="*")
  password_entry.grid(row=1, column=1, padx=10, pady=5)

  login_button = Button(login_window, text="Login", command=lambda: login(email_entry.get(), password_entry.get()))
  login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def open_sign_up_page():
    sign_up_window = Toplevel(root)
    sign_up_window.title("Sign Up")

    # Create labels and entry fields for email, password, and re-enter password
    email_label = Label(sign_up_window, text="Email:")
    email_label.grid(row=0, column=0, padx=10, pady=5)
    email_entry = Entry(sign_up_window)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = Label(sign_up_window, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = Entry(sign_up_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    reenter_password_label = Label(sign_up_window, text="Re-enter Password:")
    reenter_password_label.grid(row=2, column=0, padx=10, pady=5)
    reenter_password_entry = Entry(sign_up_window, show="*")
    reenter_password_entry.grid(row=2, column=1, padx=10, pady=5)

    # Create a sign-up button
    sign_up_button = Button(sign_up_window, text="Sign Up", command=lambda: sign_up(email_entry.get(), password_entry.get(), reenter_password_entry.get()))
    sign_up_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


def guest_login():
      ## Code to handle guest login (e.g., direct to chat support bot)
      print("Guest login")


def sign_up(email, password, confirm_password):
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match. Please try again.")
        return

    try:
        cursor.execute("INSERT INTO Users (Email, Password) VALUES (?, ?)", (email, password))
        conn.commit()
        messagebox.showinfo("Success", "Sign-up successful!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Email already exists. Please choose another.")


def login(email, password):
    cursor.execute("SELECT * FROM Users WHERE Email = ? AND Password = ?", (email, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid email or password. Please try again.")



window_width = root.winfo_screenwidth() // 5
window_height = root.winfo_screenheight() // 2
root.geometry(f"{window_width}x{window_height}")

#####Text chat for asking questions
user_input_entry = Entry(root, width=50)
user_input_entry.insert(0, "Please ask any questions regarding your problems")
user_input_entry.bind("<FocusIn>", on_click)
user_input_entry.pack(expand=True, fill='x')  # Expand horizontally



##Other buttons for more general information
business_contact_button = Button(root, text="Business Contact")
business_contact_button.pack()
tracking_information_button = Button(root, text="Track Order")
tracking_information_button.pack()




# Create buttons for different actions
login_button = Button(root, text="Login", command=open_login_page)
login_button.pack()

sign_up_button = Button(root, text="Sign Up", command=open_sign_up_page)
sign_up_button.pack()

guest_button = Button(root, text="Guest", command=guest_login)
guest_button.pack()

#run the GUI main loop
root.mainloop()
