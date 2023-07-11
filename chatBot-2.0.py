import openai

openai.api_key = "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"

messages = []
system_msg = input("What type o chat bot would you like do create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new chat bot is ready")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")