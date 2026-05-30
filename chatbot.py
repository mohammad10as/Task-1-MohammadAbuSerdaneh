def chatbot():
    responses = {
        "hello": "Hi there! How can I help you?",
        "hi": "Hey! Welcome, How can I help you?",
        "how are you": "I'm running perfectly!",
        "what is ai": "AI is the simulation of human intelligence by machines.",
        "bye": "Goodbye! Have a great day.",
        "help": "You can ask me about AI, greet me by hi or hello, or type 'quit' to exit."
    }

    print("first Chatbot — Type 'quit' to exit.")

    while True:
        raw_input_text = input("You: ")
        clean_input = raw_input_text.lower().strip()

        if clean_input == "quit":
            print("Bot: Goodbye! Session ended.")
            break

        reply = responses.get(clean_input, "I don't understand that yet. Try 'help'.")
        print(f"Bot: {reply}")

chatbot()