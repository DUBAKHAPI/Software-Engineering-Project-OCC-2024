###PROPERTY OF
###SHABEG, JOSE, NATHAN, MARSELIS, RASHA


import tkinter as tk
from tkinter import Button, Entry, Label, messagebox, Toplevel, Frame, CENTER
import openai
import sqlite3

#Set your OpenAI API key
openai.api_key = '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'


###CONNECTION TO A DATABASE, WILL MAY NEED TO SWITCH TO SQL OR MySQL
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                    UserID INTEGER PRIMARY KEY,
                    Email TEXT UNIQUE NOT NULL,
                    Password TEXT NOT NULL
                  )''')
conn.commit()


##Start of rest of code



def on_click(event):
    if user_input_entry.get() == "Please ask any questions":
        user_input_entry.delete(0, tk.END)


def start_chatbot():
    print("Welcome! The Chatbot is ready for your questions")
def send_to_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Replace model to 'gpt-3.5-turbo'
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ],
        max_tokens=100

    )
    return response['choices'][0]['message']['content'].strip()


def process_user_input():  ##adding event=none
    user_input = user_input_entry.get()
    user_input_entry.delete(0, tk.END)

    # Send user input to OpenAI for generating a response
    response = send_to_openai(user_input)

    # Display only the chatbot response in the chat window
    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, f"Chatbot: {response}\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.yview(tk.END)

#CREATE ROOT WINDOW
root = tk.Tk()
root.title("chatbot GUI")
#size and color
window_width = root.winfo_screenwidth() // 5
window_height = root.winfo_screenheight() // 2
root.geometry(f"{window_width}x{window_height}")

###BINDING THE ENTER KEY TO THE USER_INPUT_ENTRY WIDGET
user_input_entry = Entry(root, width=50, state="disabled")
user_input_entry.insert(0, "Please ask any questions regarding your problems")
user_input_entry.bind("<FocusIn>", on_click)
user_input_entry.pack(expand=True, fill='x')

#BIND THE ENTER KEY TO THE USER_INPUT_ENTRY WIDGET
user_input_entry.bind("<Return>", process_user_input)

# Chat entry and buttons initially disabled
business_contact_button = Button(root, text="Business Contact", command=lambda: display_contact_info(),
                                 state="disabled")


###DEFINING LOGIN

def open_login_page():
    login_window = Toplevel(root)
    login_window.title("Login")
    login_window.geometry("1200x800")

    # Create a frame to contain the form, which can be centered
    form_frame = Frame(login_window)
    form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Email entry
    email_label = Label(form_frame, text="Email:")
    email_label.grid(row=0, column=0, padx=10, pady=5)
    email_entry = Entry(form_frame)
    email_entry.grid(row=0, column=1, padx=10, pady=5)

    # Password entry
    password_label = Label(form_frame, text="Password:")
    password_label.grid(row=1, column=0, padx=10, pady=5)
    password_entry = Entry(form_frame, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    # Login button
    login_button = Button(form_frame, text="Login", command=lambda: login(email_entry.get(), password_entry.get()))
    login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ew")

    # Back button
    back_button = Button(form_frame, text="Back", command=login_window.destroy)
    back_button.grid(row=2, column=2, columnspan=2, padx=10, pady=5, sticky="ew")

    # Initially disable chat entry and buttons, they should be enabled after a successful login
    user_input_entry.config(state="disabled")
    business_contact_button.config(state="disabled")
    tracking_information_button.config(state="disabled")


def open_sign_up_page():
    sign_up_window = Toplevel(root)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("1200x800")

    # Create a frame to contain the form, which can be centered
    form_frame = Frame(sign_up_window)
    form_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Message at the top
    message_label = Label(form_frame, text="Please sign up to use ChatBot", font=('Arial', 14))
    message_label.grid(row=0, column=0, columnspan=2, pady=10)

    # First name entry
    first_name_label = Label(form_frame, text="First Name:")
    first_name_label.grid(row=1, column=0, padx=10, pady=5)  # Change row to 1
    first_name_entry = Entry(form_frame)
    first_name_entry.grid(row=1, column=1, padx=10, pady=5)  # Change row to 1

    # Last name entry
    last_name_label = Label(form_frame, text="Last Name:")
    last_name_label.grid(row=2, column=0, padx=10, pady=5)  # Change row to 2
    last_name_entry = Entry(form_frame)
    last_name_entry.grid(row=2, column=1, padx=10, pady=5)  # Change row to 2

    # Email entry
    email_label = Label(form_frame, text="Email:")
    email_label.grid(row=3, column=0, padx=10, pady=5)  # Change row to 3
    email_entry = Entry(form_frame)
    email_entry.grid(row=3, column=1, padx=10, pady=5)  # Change row to 3

    # Password entry
    password_label = Label(form_frame, text="Password:")
    password_label.grid(row=4, column=0, padx=10, pady=5)  # Change row to 4
    password_entry = Entry(form_frame, show="*")
    password_entry.grid(row=4, column=1, padx=10, pady=5)  # Change row to 4

    # Re-enter Password entry
    reenter_password_label = Label(form_frame, text="Re-enter Password:")
    reenter_password_label.grid(row=5, column=0, padx=10, pady=5)  # Change row to 5
    reenter_password_entry = Entry(form_frame, show="*")
    reenter_password_entry.grid(row=5, column=1, padx=10, pady=5)  # Change row to 5

    # Sign Up button
    sign_up_button = Button(form_frame, text="Sign Up",
                            command=lambda: sign_up(first_name_entry.get(), last_name_entry.get(),
                                                    email_entry.get(), password_entry.get(),
                                                    reenter_password_entry.get()))
    sign_up_button.grid(row=6, column=1, padx=10, pady=10, sticky="e")  # Change row to 6

    # Back button
    back_button = Button(form_frame, text="Back", command=sign_up_window.destroy)
    back_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")  # Change row to 6



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

        # Enable chat entry and buttons when logged in
        user_input_entry.config(state="normal")
        business_contact_button.config(state="normal")
        tracking_information_button.config(state="normal")
    else:
        messagebox.showerror("Error", "Invalid email or password. Please try again.")


def display_contact_info():
    phone_label.config(text="Phone Number: 123-456-7890")
    address_label.config(text="Address: 123 Main St, City, Country")
    email_label.config(text="Email: contact@example.com")


# Chat entry and buttons initially disabled
user_input_entry = Entry(root, width=50, state="disabled")
user_input_entry.insert(0, "Please ask any questions regarding your problems")
user_input_entry.bind("<FocusIn>", on_click)
user_input_entry.pack(expand=True, fill='x')

# Create button to send user input
send_button = Button(root, text="Enter", command=process_user_input)
send_button.pack()

business_contact_button = Button(root, text="Business Contact", command=lambda: display_contact_info(),
                                 state="disabled")
business_contact_button.pack()
tracking_information_button = Button(root, text="Track Order", state="disabled")
tracking_information_button.pack()

phone_label = Label(root, text="")
phone_label.pack()

address_label = Label(root, text="")
address_label.pack()

email_label = Label(root, text="")
email_label.pack()

# Create buttons for different actions
login_button = Button(root, text="Login", command=open_login_page)
login_button.pack()

sign_up_button = Button(root, text="Sign Up", command=open_sign_up_page)
sign_up_button.pack()


##AI INTEGRATION
# Enable chat entry and buttons
user_input_entry.config(state="normal")
business_contact_button.config(state="normal")
tracking_information_button.config(state="normal")


# Create chat display area
chat_display = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED)
chat_display.pack(expand=True, fill='both')


# Create button to send user input
send_button = Button(root, text="Send",)
send_button.pack()
# Create button to send user input
send_button.pack()


root.mainloop()
