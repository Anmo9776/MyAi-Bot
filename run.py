
import requests

API_URL = "https://free-unoficial-gpt4o-mini-api-g70n.onrender.com/"
BOT_NAME = "VoxMind"
chat_history = []

# Load training data
with open("training_data.txt", "r", encoding="utf-8") as f:
    training_data = f.read()

def ask_ai(prompt):
    global chat_history
    chat_history.append(f"User: {prompt}")
    
    # Keep only last 5 messages for memory
    memory = " ".join(chat_history[-5:])
    full_prompt = f"{training_data}\n{memory}\nAI:"

    response = requests.get(f"{API_URL}?query={full_prompt}")
    if response.status_code == 200:
        reply = response.json().get("response", "No response found.")
        chat_history.append(f"AI: {reply}")
        return reply
    else:
        return "Error: Unable to reach API."

# Simple chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print(f"{BOT_NAME}:", ask_ai(user_input))
