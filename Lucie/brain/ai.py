import ollama

def ask_ai(prompt):
    try:
        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    "role": "system",
                    "content": "You are Lucie, a smart, friendly AI assistant. Answer clearly and helpfully."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response['message']['content']

    except Exception as e:
        print("AI error:", e)
        return "I am having trouble thinking right now"