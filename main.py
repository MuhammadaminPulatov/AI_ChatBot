import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = []

print("Chat boshlandi. Chiqish uchun 'exit' deb yozing.\n")

while True:
    message = input("Siz: ").strip()

    if message.lower() == "exit":
        with open("chat_history.txt", "w", encoding="utf-8") as file:
            for role, text in chat:
                file.write(f"{role}: {text}\n")
        print("Chat saqlandi. Dastur yopildi.")
        break

    history = "\n".join([f"{role}: {text}" for role, text in chat])
    prompt = history + f"\nUser: {message}"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_text = response.text.strip()
    print("AI:", ai_text)

    chat.append(("SIZ", message))
    chat.append(("AI", ai_text))
