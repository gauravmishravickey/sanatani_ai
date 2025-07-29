# main.py
import json

def load_knowledge(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def chat_bot():
    print("🔱 Sanatani_AI Chatbot 🔱")
    print("आपका स्वागत है। कृपया अपना प्रश्न पूछें (type 'exit' to quit):\n")

    knowledge = load_knowledge("knowledge.json")

    while True:
        user_input = input("🧘‍♂️ आप: ")
        if user_input.lower() == 'exit':
            print("🚪 धन्यवाद, पुनः मिलेंगे। हर हर महादेव!")
            break
        response = knowledge.get(user_input, "❌ क्षमा करें, यह प्रश्न मेरे ज्ञान में नहीं है।")
        print("📜 उत्तर:", response)
        print()

if __name__ == "__main__":
    chat_bot()
