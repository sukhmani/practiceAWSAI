from chat_memory import add_message, get_messages
from claude_client import invoke_claude_model

def main():
    print("Claude Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        add_message("user", user_input)
        response = invoke_claude_model(get_messages())
        add_message("assistant", response['content'][0]['text'])

        print("Claude:", response['content'][0]['text'])

if __name__ == "__main__":
    main()
