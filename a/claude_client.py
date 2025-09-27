import json

def invoke_claude_model(messages):
    """
    Simulates Claude 3 Sonnet response using message history.
    Replace this with real Bedrock call when ready.
    """
    last_user_message = messages[-1]['content'][0]['text']
    mock_response = "Claude would reply to: " + last_user_message

    return {
        "role": "assistant",
        "content": [{"type": "text", "text": mock_response}]
    }
