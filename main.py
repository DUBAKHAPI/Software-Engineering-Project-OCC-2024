# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def chatbot():
  while True:
    user_input = input("You: ").lower()
    if user_input == "hello":
      print("Bot: Hi there!")
    elif user_input == "bye":
      print("Bot: Goodbye!")
      break
    else:
      print("Bot: I'm sorry, I don't understand.")


if __name__ == "__main__":
  print("Bot: Hello! I'm your chatbot.")
  chatbot()

# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
