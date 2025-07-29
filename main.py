import json
import streamlit as st
import torch
import warnings
from sentence_transformers import SentenceTransformer, util
import re

# 🚫 FutureWarning को suppress करें
warnings.filterwarnings("ignore", category=FutureWarning)

# 📚 JSON लोड करें
with open("qa_data.json", "r", encoding="utf-8") as file:
    qa_data = json.load(file)

# 🧠 NLP Model
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# 🔠 Normalize Function
def normalize(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = text.replace("kaun", "koun").replace("koun", "kaun")
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# ✨ Streamlit UI Config
st.set_page_config(page_title="🔱 Sanatani_AI", layout="centered")

# 🧡 Custom CSS
st.markdown("""
<style>
body {
    background-color: #fffaf0;
}
h1 {
    color: #d84315;
    text-align: center;
}
.stTextInput>div>div>input {
    font-size: 18px;
    padding: 10px;
}
.stButton>button {
    font-size: 18px;
    background-color: #f57c00;
    color: white;
    border-radius: 8px;
    padding: 8px 16px;
}
.chat-box {
    background-color: #fff3e0;
    border-radius: 12px;
    padding: 15px;
    margin-top: 10px;
    font-size: 18px;
    border-left: 5px solid #fb8c00;
}
.user-question {
    background-color: #e3f2fd;
    border-left: 5px solid #42a5f5;
    margin-top: 15px;
    padding: 12px;
    border-radius: 12px;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)

# 🌟 Title
st.markdown("<h1>🔱 Sanatani_AI Chatbot 🔱</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>🙏 आपका स्वागत है, कृपया अपना प्रश्न नीचे पूछें:</p>", unsafe_allow_html=True)

# NLP Q&A Preprocessing
raw_questions = list(qa_data.keys())
normalized_questions = [normalize(q) for q in raw_questions]
question_embeddings = model.encode(normalized_questions, convert_to_tensor=True)

# 🧑‍💻 User Input
user_question = st.text_input("✍️ प्रश्न लिखें:")

if user_question:
    st.markdown(f"<div class='user-question'>🙋‍♂️ <strong>आप:</strong> {user_question}</div>", unsafe_allow_html=True)

    norm_user_q = normalize(user_question)
    user_embedding = model.encode(norm_user_q, convert_to_tensor=True)

    similarities = util.pytorch_cos_sim(user_embedding, question_embeddings)[0]
    best_match_idx = torch.argmax(similarities).item()

    best_match_question = raw_questions[best_match_idx]
    answer = qa_data[best_match_question]

    st.markdown(f"<div class='chat-box'>🕉️ <strong>Sanatani_AI:</strong> {answer}</div>", unsafe_allow_html=True)
