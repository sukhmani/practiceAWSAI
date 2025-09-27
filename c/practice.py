messages =[]

user_input = input("enter: ")

messages.append({
    "role": "user",
    "content": [{"type": "text", "text": user_input}]
})

reply = "Claude would reply to: " + user_input

messages.append({
    "role": "assistant",
    "content": [{"type": "text", "text": reply}]
})

print("Claude:", reply)
