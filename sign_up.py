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