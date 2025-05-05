
import openai

# API Key
openai.api_key = "Insert API Key here"

def chat_with_gpt():
    print("Welcome to GPT 3.5 Turbo! Type 'exit' to quit.\n")
    while True:
        #user
        user_input = input("User: ")

        #code to cancel
        if user_input.lower() == "cancel AI":
            print("Abort!")
            break

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Or "gpt-4" if available
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            #Chat history
            chat_history = [
                {"role": "system", "content": "You are a helpful assistant."}
            ]

            while True:
                user_input = input("User: ")
                if user_input.lower() == "cancel AI":
                    print("Abort!")
                    break


                chat_history.append({"role": "user", "content": user_input})

                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=chat_history
                    )
                    reply = response['choices'][0]['message']['content']
                    print("Bot:", reply)


                    chat_history.append({"role": "assistant", "content": reply})

                except Exception as e:
                    print("Error:", e)

            if __name__ == "__main__":
                chat_with_gpt()
