import os
from datetime import datetime
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = []

timestamp = datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
filename = f"chat_{timestamp}.txt"

print("Chat boshlandi. Chiqish uchun 'exit' deb yozing.\n")

while True:
    message = input("Siz: ").strip()

    if message.lower() == "exit":
        print(f"Chat saqlandi: {filename}. Dastur yopildi.")
        break

    chat.append(("SIZ", message))

    history = "\n".join([f"{role}: {text}" for role, text in chat])
    prompt = history + f"\n\nIltimos, javobni faqat O'zbek tilida yozing."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_text = response.text.strip()
    print("AI:", ai_text)
    chat.append(("AI", ai_text))

    with open(filename, "w", encoding="utf-8") as file:
        for role, text in chat:
            file.write(f"{role}: {text}\n")
