responses = {
    "hi": "Hello!",
    "hello": "Hi there! Welcome to the AI Chatbot.",
    "help": "Try: hi, hello, ai, python, internship, name, thanks, bye",
    "name": "I'm a Rule-Based AI Chatbot.",
    "ai": "AI stands for Artificial Intelligence.",
    "python": "Python is widely used for AI development.",
    "internship": "Welcome to the DecodeLabs AI Internship!",
    "thanks": "You're welcome!",
    "bye": "Goodbye!"
}
print("=== Rule-Based AI Chatbot ===")
print("Type 'exit' to quit.\n")
while True:
    user = input("You: ").strip().lower()
    if user == "exit":
        print("Bot: Goodbye!")
        break
    print("Bot:", responses.get(user, "I don't understand."))