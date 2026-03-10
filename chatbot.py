print("Simple Chatbot")

while True:
    user_input = input("You: ")

    if user_input.lower() == "hello":
        print("Bot: Hello! How can I help you?")

    elif user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand that yet.")