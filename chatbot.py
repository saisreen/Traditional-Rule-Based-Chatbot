from datetime import datetime

print("===================================")
print(" Welcome to the Traditional Chatbot ")
print("===================================")
print("Type 'help' to see what I can do.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you today?")

    elif user_input == "what is your name":
        print("Bot: My name is StudentBot.")

    elif user_input == "help":
        print("Bot: I can answer:")
        print("- Greetings")
        print("- My name")
        print("- Date")
        print("- Time")
        print("- Goodbye")

    elif user_input == "date":
        print("Bot:", datetime.now().strftime("%B %d, %Y"))

    elif user_input == "time":
        print("Bot:", datetime.now().strftime("%I:%M %p"))

    elif user_input in ["bye", "exit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")