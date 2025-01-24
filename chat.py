import os
import openai


API_KEY = os.getenv("OPENAI_API_KEY")


openai.api_key = API_KEY

def chatbot():
    messages = [{"role": "system", "content": "Thank you chatbot!!!."}]

    while True:
        message = input("User: ")

        if message.lower() == 'quit':
            break
        if not message.strip():
            print("Please enter a valid message.")
            continue

        messages.append({"role": "user", "content": message})

        try:
            
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=messages
            )
            chat_message = response['choices'][0]['message']['content']
            print(f"Bot: {chat_message}")
            messages.append({"role": "assistant", "content": chat_message})
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Start chatting with the bot (type 'quit' to stop)!")
    chatbot()
