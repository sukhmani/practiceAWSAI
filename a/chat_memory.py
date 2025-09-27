messages = []

def add_message(role, text):
    """
    Adds a message to the conversation history.
    role: 'user' or 'assistant'
    text: message content
    """
    messages.append({
        "role": role,
        "content": [{"type": "text", "text": text}]
    })

def get_messages():
    return messages
