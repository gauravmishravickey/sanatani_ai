# 🔱 Sanatani_AI Chatbot - Ready to Run Version
import json

def load_data():
    with open("data/sanatani_data.json", "r", encoding="utf-8") as f:
        return json.load(f)

def chatbot():
    data = load_data()
    print("🔱 Sanatani_AI Chatbot 🔱")
    print("आपका स्वागत है। कृपया अपना प्रश्न पूछें (type 'exit' to quit):\n")
    while True:
        user_input = input("🧘‍♂️ आप: ").strip().lower()
        if user_input in ["exit", "quit", "bye"]:
            print("🙏 धन्यवाद! जय श्रीराम 🚩")
            break
        response = data.get(user_input, "❌ क्षमा करें, यह प्रश्न मेरे ज्ञान में नहीं है।")
        print("🔆 उत्तर:", response)

if __name__ == "__main__":
    chatbot()