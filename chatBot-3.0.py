import openai
import gradio

openai.api_key="YourApiKey"

messages = [{"role": "system", "content": "you are a psychologist"}]

def CustomGPT(UserInput):
    messages.append({"role": "user", "content": UserInput})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )

    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomGPT, inputs= "text", outputs="text", title="chat muito foda")

demo.launch(share=True)
