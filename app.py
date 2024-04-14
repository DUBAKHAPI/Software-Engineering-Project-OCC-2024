import tkinter as tk
from tkinter import *
import mysql.connector


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
    resetResetPasswordPage()  # Reset the reset password page


def resetResetPasswordPage():
    resetPage_username_entry.delete(0, tk.END)  # Clear the entry field
    resetPage_result_label.config(text="", fg="grey")  # Hide the red text


def ResetPassword():
    print("Reset Password button clicked")
    resetPage_result_label.config(
        text="An email has been sent if the account exists. Please check your email and follow the instructions.",
        fg="red")
    resetPage_result_label.grid(row=4, column=0, columnspan=2, pady=10)
    resetPage_reset_button.grid_forget()
    resetPage_mainMenu_button.grid(row=5, column=0, columnspan=2, pady=10)


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
    # If the default text is present, delete it
    if chatAreaPage_typing_area.get("1.0", "end-1c") == "Type your message here":
        chatAreaPage_typing_area.delete("1.0", tk.END)
        chatAreaPage_typing_area.config(fg="black")


def toRequestAgentSupport():
    chatAreaPage.pack_forget()  # hides chat session
    supportTicketPage.pack()  # shows ticket page


def EndSession():
    print("remember add Sign Out portion command")
    chatAreaPage.pack_forget()  # Hide the chat area page
    supportTicketPage.pack_forget()  # Hide the support ticket page
    mainMenuPage.pack()  # Show the Main Menu
# ------------App Functions end----------------


# ------------Database Functions----------------
def PassMessageLog():
    print("hello")


def PassUnknownTextLog():
    print("hello")


def SubmitTicket():
    print("hello")


def VerifyLogIn():
    print("hello")


def GetFaqURl():
    print("hello")


def AddUser():
    print("hello")


def ResetPassword():
    print("hello")
# ------------Database Functions End----------------


# ------------AI Functions----------------


# ------------AI Functions End----------------

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

loginPage_username_label = tk.Label(loginPage, text="Username:", font=("Helvetica", 12), bg="grey")
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
signUpPage_first_name_entry = tk.Entry(signUpPage_form_frame)
signUpPage_first_name_entry.grid(row=1, column=1, padx=10, pady=5)

# Last name entry
signUpPage_last_name_label = tk.Label(signUpPage_form_frame, text="Last Name:", bg="grey")
signUpPage_last_name_label.grid(row=2, column=0, padx=10, pady=5)
signUpPage_last_name_entry = tk.Entry(signUpPage_form_frame)
signUpPage_last_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Email entry
signUpPage_email_label = tk.Label(signUpPage_form_frame, text="Email:", bg="grey")
signUpPage_email_label.grid(row=3, column=0, padx=10, pady=5)
signUpPage_email_entry = tk.Entry(signUpPage_form_frame)
signUpPage_email_entry.grid(row=3, column=1, padx=10, pady=5)

# Password entry
signUpPage_password_label = tk.Label(signUpPage_form_frame, text="Password:", bg="grey")
signUpPage_password_label.grid(row=4, column=0, padx=10, pady=5)
signUpPage_password_entry = tk.Entry(signUpPage_form_frame, show="*")
signUpPage_password_entry.grid(row=4, column=1, padx=10, pady=5)

# Re-enter Password entry
signUpPage_reenter_password_label = tk.Label(signUpPage_form_frame, text="Re-enter Password:", bg="grey")
signUpPage_reenter_password_label.grid(row=5, column=0, padx=10, pady=5)
signUpPage_reenter_password_entry = tk.Entry(signUpPage_form_frame, show="*")
signUpPage_reenter_password_entry.grid(row=5, column=1, padx=10, pady=5)

# Sign Up button
signUpPage_sign_up_button = tk.Button(signUpPage_form_frame, text="Sign Up", font=("Helvetica", 12, "bold"))
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
chatAreaPage_chat_area = tk.Text(chatAreaPage_chat_frame, bg="white", bd=0, wrap=tk.WORD, fg="grey", height=24)
chatAreaPage_chat_area.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=200, pady=(50, 0))

# Create a frame for typing area
chatAreaPage_typing_frame = tk.Frame(chatAreaPage_chat_frame, bg="white", bd=2, relief=tk.SUNKEN)
chatAreaPage_typing_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Create a typing area for user input
chatAreaPage_typing_area = tk.Text(chatAreaPage_typing_frame, bg="white", bd=0, wrap=tk.WORD, height=4, fg="grey")
chatAreaPage_typing_area.insert(tk.END, "Type your message here")
chatAreaPage_typing_area.bind("<Button-1>", on_click_typing)  # Bind click event to typing_area
chatAreaPage_typing_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 0), pady=(10, 0))

# Create a send button
chatAreaPage_send_button = tk.Button(chatAreaPage_typing_frame, text="Send", fg="black", font=("Helvetica", 12, "bold"),
                                     bd=2, relief=tk.RAISED)
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
                                        font=("Helvetica", 12, "bold"), bd=2, relief=tk.RAISED)
supportTicket_submit_button.grid(row=3, column=1, columnspan=2, pady=10, padx=10, sticky='ew')
# ------------Support Ticket Page End----------------


# ------------Database Implementation----------------
aiDB = mysql.connector.connect(host="localhost", user="root",passwd="root")

# ------------Database Implementation End----------------


mainMenuPage.tkraise()
win.mainloop()
