import tkinter as tk
from tkinter import *
import openai
from tkinter import messagebox
import pymysql
import pymysql.cursors
import datetime
import os



#Set your OpenAI API key
openai.api_key = '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'


messages = []

#Setting the parameters in which the ai will respond
system_content = '''You are a customer service chat bot that is know as HelpBot.
You will respond only to greetings and any questions pertaining to customer services the system offers. 
For any questions that do not fall within these parameters you will respond with "Unfortunately I cannot help with that 
would you like to start a support ticket.".'''

users_name = ""
userid = ""
filepath = ""
counter = 0
# ------------App Functions----------------


def toPageLogin():
    mainMenuPage.pack_forget()  # Hide the main menu page
    loginPage.pack()  # Show the login page


def toPageSignUp():
    mainMenuPage.pack_forget()  # Hide the main menu page
    loginPage.pack_forget()  # Hide the login page
    resetPasswordPage.pack_forget()  # Hide the reset password page
    chatAreaPage.pack_forget()  # Hide the chat area page
    signUpPage.pack()  # Show the signup page


def Login():
    print("Login button Clicked")
    loginPage.pack_forget()  # hides the login page
    chatAreaPage.pack()  # Shows chat area


def toChatAreaPage():
    supportTicketPage.pack_forget()  # hides the submit ticket page
    chatAreaPage.pack()  # shows the chat area page


def toResetPassword():
    loginPage.pack_forget()  # Hide the login page
    mainMenuPage.pack_forget()  # Hide the main menu page
    resetPasswordPage.pack()  # Show the Reset Password Page


def ResetPassword():
    # Display an information message indicating that an email has been sent
    messagebox.showinfo("Email Sent", "An Email has been to your email with instructions on how to proceed")

    # Hide the reset button and show the main menu button
    resetPage_reset_button.grid_forget()
    resetPage_mainMenu_button.grid(row=5, column=0, columnspan=2, pady=10)

    # Show the main menu page and hide the reset password page
    mainMenuPage.pack()
    resetPasswordPage.pack_forget()

    resetPage_username_entry.delete(0, tk.END)  # Clear the username entry field


def toMainMenu():
    loginPage.pack_forget()  # Hide the login page
    signUpPage.pack_forget()  # Hide the Sign-Up page
    resetPasswordPage.pack_forget()  # Hide the reset password page
    mainMenuPage.pack()  # Show the main menu page
    resetPage_mainMenu_button.grid_forget()  # Hide Main Menu button on the reset password page
    resetPage_reset_button.grid(row=3, column=0,
                                columnspan=2, pady=20)  # Show Reset Password button on the reset password page


def on_click_typing(event):
    """Function to handle click event on the typing area"""
    if chatAreaPage_typing_area.get("1.0", "end-1c") == "Type your message here": # Check if the default text is present
        chatAreaPage_typing_area.delete("1.0", tk.END) # If present, delete the default text
        chatAreaPage_typing_area.config(fg="black")  # Change text color to black (assumed to be default)


def toRequestAgentSupport():
    chatAreaPage.pack_forget()  # hides chat session
    supportTicketPage.pack()  # shows ticket page


def EndSession():
    # Clear the chat area display
    chatAreaPage_chat_area.delete("1.0", tk.END)

    chatAreaPage.pack_forget()  # Hide the chat area page
    supportTicketPage.pack_forget()  # Hide the support ticket page
    mainMenuPage.pack()  # Show the Main Menu
    PassMessageLog()

def delete_file(filepath):
    file_path = filepath
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        messagebox.showinfo("Jose Sucks", "Jose Fucked Something Up")
# ------------App Functions end----------------


# ------------Database Functions----------------
def signup():
    # Create a connection to the database
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="paulsucks01!",
        database="chatterbot",
    )
    # Create a cursor object to execute SQL queries
    myCursor = con.cursor()

    # Retrieve user input from entry fields
    firstname = signUpPage_first_name_entry.get()
    lastname = signUpPage_last_name_entry.get()
    email = signUpPage_email_entry.get()
    password = signUpPage_password_entry.get()

    # Generate a username from the email address
    username = email.split("@")[0]

    # Check if the email already exists in the database
    DuplicateSignUpQuery = 'select * from users where email = %s'
    myCursor.execute(DuplicateSignUpQuery, email)
    row = myCursor.fetchone()

    if row != None:
        # If the email already exists, show a messagebox indicating duplicate email
        messagebox.showinfo("Duplicate", "Duplicate Email")
    else:
        # If the email is unique, insert the user data into the database
        messagebox.showinfo("Sign Up Successful", "Sign Up was succesful")
        signInQuery = 'INSERT INTO users (username, first_name, last_name, email, password) VALUES (%s, %s, %s, %s, %s)'
        myCursor.execute(signInQuery, (username, firstname, lastname, email, password))
        con.commit()
        con.close()

        # Hide the signup page and show the login page
        loginPage.pack()
        signUpPage.pack_forget()

        # Clear the entry fields
        signUpPage_first_name_entry.delete(0, tk.END)
        signUpPage_last_name_entry.delete(0, tk.END)
        signUpPage_email_entry.delete(0, tk.END)
        signUpPage_password_entry.delete(0, tk.END)


def Login():
    # Create a connection to the database
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="paulsucks01!",
        database="chatterbot",
    )
    # Create a cursor object to execute SQL queries
    myCursor = con.cursor()

    # Retrieve username/email and password from entry fields
    username_email = loginPage_username_entry.get()
    password = loginPage_password_entry.get()

    # Query to check if the provided username/email and password match a record in the database
    logInQuery = 'select * from users where (username = %s or email = %s) and password = %s'
    myCursor.execute(logInQuery, (username_email, username_email, password))
    row = myCursor.fetchone()

    # Check if a row was returned, indicating successful login
    if row == None:
        # If no row was returned, show a messagebox indicating invalid credentials
        messagebox.showinfo("Invalid", "Invalid Username/Email or Password")
    else:
        # If a row was returned, hide the login page and show the chat area
        loginPage.pack_forget()
        chatAreaPage.pack()

        # Clear the entry fields
        loginPage_username_entry.delete(0, tk.END)
        loginPage_password_entry.delete(0, tk.END)
        getUserQuery = 'select * from users where (username = %s or email = %s) and password = %s'
        myCursor.execute(getUserQuery, (username_email, username_email, password))
        row = myCursor.fetchone()
        getUsersName(row[2])
        getUserID(row[0])
        con.close()


def getUsersName(firstname):
    global users_name
    users_name = firstname


def getUserID(user_id):
    global userid
    userid = user_id


def PassMessageLog():
    global userid
    global filepath
    filepath = "messagelog.txt"
    # Read the content of the messagelog.txt file
    with open("messagelog.txt", "r") as log_file:
        message_logs = log_file.read()

    # Create a connection to the database
    con = pymysql.connect(
        host="localhost",
        user="root",
        password="paulsucks01!",
        database="Chatterbot"
    )
    current_datetime = datetime.datetime.now()
    # Create a cursor object to execute SQL queries
    myCursor = con.cursor()
    PassMessageLogQuery = 'INSERT INTO messagelogs (logDT, message_logs, user_id) ' \
                          'VALUES (%s, %s, %s)'
    myCursor.execute(PassMessageLogQuery, (current_datetime, message_logs, userid))
    con.commit()
    con.close()
    delete_file(filepath)


def PassUnknownTextLog():
    print("hello")


def SubmitTicket():
    global userid
    global filepath
    filepath = "supportticket.txt"
    # Retrieve user inputs from the text boxes
    issue = supportTicket_issue_text.get("1.0", tk.END).strip()
    description = supportTicket_description_text.get("1.0", tk.END).strip()

    if issue and description:
        # Format the inputs
        formatted_issue = f"issue: {issue}"
        formatted_description = f"description: {description}"

        # Write the formatted inputs to the support ticket file
        with open("supportticket.txt", "a") as ticket_file:
            ticket_file.write(formatted_issue + "\n")
            ticket_file.write(formatted_description + "\n")

        # Read the content of the file
        with open("supportticket.txt", "r") as ticket_file:
            ticket_content = ticket_file.read()

        # Create a connection to the database
        con = pymysql.connect(
            host="localhost",
            user="root",
            password="paulsucks01!",
            database="chatterbot",
        )

        current_datetime = datetime.datetime.now()
        # Create a cursor object to execute SQL queries
        myCursor = con.cursor()
        PassSupportTicketQuery = 'INSERT INTO supporttickets (status, openDT, supportticket, user_id) ' \
                                 'VALUES (%s, %s, %s, %s)'
        myCursor.execute(PassSupportTicketQuery, ("open", current_datetime, ticket_content, userid))
        con.commit()
        con.close()
        # Clear the text boxes after submitting the ticket
        supportTicket_issue_text.delete("1.0", tk.END)
        supportTicket_description_text.delete("1.0", tk.END)

        # Show a messagebox indicating successful submission
        messagebox.showinfo("Ticket Submitted", "Your ticket has been submitted successfully.")
        delete_file(filepath)
    else:
        # Show a messagebox if any of the text boxes are empty
        messagebox.showwarning("Empty Fields"
                               , "Please fill in both the issue and description fields before submitting.")


def VerifyLogIn():
    print("hello")


def GetFaqURl():
    print("hello")


def AddUser():
    print("hello")


def ResetPasswordEmail():
    print("hello")


def sendMessage():
    global counter
    global users_name
    # Get the message from the typing area
    message = chatAreaPage_typing_area.get("1.0", tk.END).strip()

    if message:
        # Format the message as "user: message"
        formatted_message = f"{users_name}: {message}"

        # Append the formatted message to the message display portion
        chatAreaPage_chat_area.insert(tk.END, formatted_message + "\n")

        # Scroll to the end of the chat area to show the latest message
        chatAreaPage_chat_area.see(tk.END)

        # Write the formatted message along with the current date and time to the message log file
        with open("messagelog.txt", "a") as log_file:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{timestamp}: {formatted_message}\n")

        # Get AI response
        ai_response = ask_openai(message)
        response_message = f"HelpBot: {ai_response}"
        chatAreaPage_chat_area.insert(tk.END, response_message + "\n")

        # Clear the typing area after sending the message
        chatAreaPage_typing_area.delete("1.0", tk.END)
        counter+=1
    else:
        # Show a messagebox if the user tries to send an empty message
        messagebox.showinfo("Empty Message", "Please enter a message before sending.")

        #clear tpying area after
# ------------Database Functions End----------------


# ------------AI Functions----------------
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error communicating with OpenAI: {str(e)}")
        return f"Sorry, I am unable to process your request right now due to: {str(e)}"
# ------------AI Functions End----------------


# ------------Creates Initial Window and Frames----------------
win = tk.Tk()
win.geometry("1200x800")
win.title("Chatterbot Support")
win.configure(bg="grey")

# Create frames for different pages
mainMenuPage = tk.Frame(win, bg="grey")
loginPage = tk.Frame(win, bg="grey")
signUpPage = tk.Frame(win, bg="grey")
resetPasswordPage = tk.Frame(win, bg="grey")
chatAreaPage = tk.Frame(win, bg="grey")
supportTicketPage = tk.Frame(win, bg="grey")
# ------------Initial Window and Frames End----------------


# ------------Main Menu----------------
# Create labels for Main Menu
mainMenu_welcome_label = tk.Label(mainMenuPage, text="Welcome to Chatter Bot Support", font=("Helvetica", 24, "bold"),
                                  bg="grey")
mainMenu_welcome_label.grid(row=0, column=0, pady=100, columnspan=2)

# Create login button for Main Menu
mainMenu_login_button = tk.Button(mainMenuPage, text="Login", font=("Helvetica", 16, "bold"), command=toPageLogin,
                                  width=20)
mainMenu_login_button.grid(row=1, column=0, padx=20, pady=20)

# Create sign up button for Main Menu
mainMenu_signup_button = tk.Button(mainMenuPage, text="Sign Up", font=("Helvetica", 16, "bold"), command=toPageSignUp,
                                   width=20)
mainMenu_signup_button.grid(row=1, column=1, padx=20, pady=20)

# Show the main menu page
mainMenuPage.pack()
# ------------Main Menu END----------------


# ------------Login Page----------------
# Create labels for Login Page
loginPage_welcome_label = tk.Label(loginPage, text="Welcome to Chatter Bot Support", font=("Helvetica", 24, "bold"),
                                   bg="grey")
loginPage_welcome_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create login section
loginPage_login_label = tk.Label(loginPage, text="Login", font=("Helvetica", 16, "bold"), bg="grey")
loginPage_login_label.grid(row=1, column=0, columnspan=2, pady=10)

loginPage_username_label = tk.Label(loginPage, text="Username or Email:", font=("Helvetica", 12), bg="grey")
loginPage_username_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)

loginPage_username_entry = tk.Entry(loginPage, font=("Helvetica", 12))
loginPage_username_entry.grid(row=2, column=1, sticky="w", padx=20, pady=10)

loginPage_password_label = tk.Label(loginPage, text="Password:", font=("Helvetica", 12), bg="grey")
loginPage_password_label.grid(row=3, column=0, sticky="e", padx=20, pady=10)

loginPage_password_entry = tk.Entry(loginPage, show="*", font=("Helvetica", 12))
loginPage_password_entry.grid(row=3, column=1, sticky="w", padx=20, pady=10)

loginPage_login_button = tk.Button(loginPage, text="Login", font=("Helvetica", 16, "bold"), command=Login)
loginPage_login_button.grid(row=4, column=0, columnspan=2, pady=20)

loginPage_reset_button = tk.Button(loginPage, text="Reset Password", font=("Helvetica", 16, "bold"),
                                   command=toResetPassword)
loginPage_reset_button.grid(row=5, column=0, columnspan=2, pady=10)

loginPage_menu_button = tk.Button(loginPage, text="Main Menu", font=("Helvetica", 16, "bold"), command=toMainMenu)
loginPage_menu_button.grid(row=6, column=0, columnspan=2, pady=10)
# ------------Login Page End----------------


# ------------Sign Up Page----------------
# Message at the top
signUpPage_message_label = tk.Label(signUpPage, text="Please sign up to use ChatBot", font=("Helvetica", 14)
                                    , bg="grey")
signUpPage_message_label.grid(row=0, column=0, columnspan=2, pady=10)

# Create a frame to contain the form, which can be centered
signUpPage_form_frame = tk.Frame(signUpPage, bg="grey")
signUpPage_form_frame.grid(row=1, column=0, columnspan=2)

# First name entry
signUpPage_first_name_label = tk.Label(signUpPage_form_frame, text="First Name:", bg="grey")
signUpPage_first_name_label.grid(row=1, column=0, padx=10, pady=5)
signUpPage_first_name_entry = tk.Entry(signUpPage_form_frame, width=30)
signUpPage_first_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Last name entry
signUpPage_last_name_label = tk.Label(signUpPage_form_frame, text="Last Name:", bg="grey")
signUpPage_last_name_label.grid(row=2, column=0, padx=10, pady=5)
signUpPage_last_name_entry = tk.Entry(signUpPage_form_frame, width=30)
signUpPage_last_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

# Email entry
signUpPage_email_label = tk.Label(signUpPage_form_frame, text="Email:", bg="grey")
signUpPage_email_label.grid(row=3, column=0, padx=10, pady=5)
signUpPage_email_entry = tk.Entry(signUpPage_form_frame, width=30)
signUpPage_email_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Password entry
signUpPage_password_label = tk.Label(signUpPage_form_frame, text="Password:", bg="grey")
signUpPage_password_label.grid(row=4, column=0, padx=10, pady=5)
signUpPage_password_entry = tk.Entry(signUpPage_form_frame, width=30)
signUpPage_password_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Sign Up button
signUpPage_sign_up_button = tk.Button(signUpPage_form_frame, text="Sign Up", font=("Helvetica", 12, "bold"),
                                      command=signup)
signUpPage_sign_up_button.grid(row=6, column=1, padx=10, pady=10, sticky="e")

# Back button
signUpPage_back_button = tk.Button(signUpPage_form_frame, text="Main Menu", font=("Helvetica", 12, "bold"),
                                   command=toMainMenu)
signUpPage_back_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")
# ------------Sign Up Page End----------------


# ------------Rest Password Page----------------
# Create label for page title
resetPage_title_label = tk.Label(resetPasswordPage, text="Chatterbot Reset Password", font=("Helvetica", 24, "bold"),
                                 bg="grey")
resetPage_title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create label for instruction
resetPage_instruction_label = tk.Label(resetPasswordPage,
                                       text="Please enter your username or email and hit reset password button",
                                       font=("Helvetica", 12), bg="grey")
resetPage_instruction_label.grid(row=1, column=0, columnspan=2, pady=10)

# Create label and entry for username/email
resetPage_username_label = tk.Label(resetPasswordPage, text="Username/Email:", font=("Helvetica", 12), bg="grey")
resetPage_username_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)

resetPage_username_entry = tk.Entry(resetPasswordPage, font=("Helvetica", 12))
resetPage_username_entry.grid(row=2, column=1, sticky="w", padx=20, pady=10)

resetPage_reset_button = tk.Button(resetPasswordPage, text="Reset Password", font=("Helvetica", 16, "bold"),
                                   command=ResetPassword)
resetPage_reset_button.grid(row=3, column=0, columnspan=2, pady=20)

resetPage_mainMenu_button = tk.Button(resetPasswordPage, text="Main Menu", font=("Helvetica", 16, "bold"),
                                      command=toMainMenu)

# Create label to display reset password result
resetPage_result_label = tk.Label(resetPasswordPage, text="", font=("Helvetica", 12), bg="grey")
resetPage_result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Initially hide the Main Menu button
resetPage_mainMenu_button.grid_forget()
# ------------Reset Password Page End----------------


# ------------Chat Area Page----------------
# Create a frame for the chat area
chatAreaPage_chat_frame = tk.Frame(chatAreaPage, bg="white", width=800, height=800, highlightbackground="black",
                                   highlightthickness=2)
chatAreaPage_chat_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Create a scrollable text widget for displaying messages
chatAreaPage_chat_area = tk.Text(chatAreaPage_chat_frame, bg="white", bd=0, wrap=tk.WORD, fg="black", height=24)
chatAreaPage_chat_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=200, pady=(50, 0))

# Create a frame for typing area
chatAreaPage_typing_frame = tk.Frame(chatAreaPage_chat_frame, bg="white", bd=2, relief=tk.SUNKEN)
chatAreaPage_typing_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create a typing area for user input
chatAreaPage_typing_area = tk.Text(chatAreaPage_typing_frame, bg="white", bd=0, wrap=tk.WORD, height=4, fg="grey")
chatAreaPage_typing_area.insert(tk.END, "Type your message here")  # Placeholder text
chatAreaPage_typing_area.bind("<Button-1>", on_click_typing)  # Bind click event to typing_area
chatAreaPage_typing_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(10, 0))

# Create a send button
chatAreaPage_send_button = tk.Button(chatAreaPage_typing_frame, text="Send", fg="black", font=("Helvetica", 12, "bold"),
                                     bd=2, relief=tk.RAISED, command=sendMessage)
chatAreaPage_send_button.pack(side=tk.RIGHT, padx=(0, 10), pady=(10, 0))

# Create a frame for buttons
chatAreaPage_button_frame = tk.Frame(chatAreaPage, bg='grey')
chatAreaPage_button_frame.grid(row=1, column=0, columnspan=2, pady=10)

# Create the "Request Live Agent Support" button
chatAreaPage_request_button = tk.Button(chatAreaPage_button_frame, text="Request Agent Support",
                                        command=toRequestAgentSupport, fg="black", font=("Helvetica", 12, "bold"), bd=2,
                                        relief=tk.RAISED)
chatAreaPage_request_button.pack(side=tk.LEFT, padx=(10, 5))

# Create the "End Session" button
chatAreaPage_end_button = tk.Button(chatAreaPage_button_frame, text="End Session", command=EndSession, fg="black",
                                    font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED)
chatAreaPage_end_button.pack(side=tk.RIGHT, padx=(5, 10))
# ------------Chat Area Page End----------------


# ------------Support Ticket Page----------------
# Create label for "issue"
supportTicket_issue_label = tk.Label(supportTicketPage, text="ISSUE:", font=("Helvetica", 12, "bold"), bg="grey")
supportTicket_issue_label.grid(row=0, column=0, sticky="w", padx=20, pady=10)

# Create text box for input
supportTicket_issue_text = tk.Text(supportTicketPage, height=1, width=50)
supportTicket_issue_text.grid(row=0, column=1, sticky="w", padx=10, pady=10)

# Create label for "description"
supportTicket_description_label = tk.Label(supportTicketPage, text="DESCRIPTION:", font=("Helvetica", 12, "bold"),
                                           bg="grey")
supportTicket_description_label.grid(row=1, column=0, sticky="w", padx=20, pady=10)

# Create text box for description
supportTicket_description_text = tk.Text(supportTicketPage, height=40, width=100)
supportTicket_description_text.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)

# Create "Return to Chat Session" button
supportTicket_return_button = tk.Button(supportTicketPage, text="Return to Chat Session",
                                        font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED, command=toChatAreaPage)
supportTicket_return_button.grid(row=2, column=1, pady=10, padx=10, sticky='ew')

# Create "Main Menu" button
supportTicket_main_menu_button = tk.Button(supportTicketPage, text="End Session",
                                           font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED, command=EndSession)
supportTicket_main_menu_button.grid(row=2, column=2, pady=10, padx=10, sticky='ew')

# Create "Submit Ticket" button
supportTicket_submit_button = tk.Button(supportTicketPage, text="Submit Ticket",
                                        font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED, command=SubmitTicket)
supportTicket_submit_button.grid(row=3, column=1, columnspan=2, pady=10, padx=10, sticky='ew')
# ------------Support Ticket Page End----------------


# ------------Database Implementation----------------

# ------------Database Implementation End----------------

mainMenuPage.tkraise()
win.mainloop()
