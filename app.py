from flask import Flask, render_template, request, jsonify
import json
import re
from datetime import datetime
import random

app = Flask(__name__)

with open("rules.json", encoding="utf-8") as f:
    rules = json.load(f)

# Basic knowledge base (can answer general questions)
knowledge_base = {
    "what is python": "Python is a programming language used for web, AI, and automation.",
    "what is ai": "AI stands for Artificial Intelligence. It enables machines to think and learn.",
    "what is machine learning": "Machine learning is a part of AI that allows systems to learn from data.",
    "what is chatbot": "A chatbot is a software that simulates conversation with users.",
    "who is the prime minister of india": "The Prime Minister of India is Narendra Modi."
}

# Smart fallback responses
fallback_responses = [
    "That's an interesting question 🤔",
    "I'm still learning, but I will improve 🚀",
    "Can you ask in a different way?",
    "I don’t have exact answer yet, but I'm learning!"
]

def get_response(user_input):
    user_input = user_input.lower()

    # 1️⃣ Rule-based matching
    for rule in rules:
        for pattern in rule["patterns"]:
            if re.search(pattern, user_input):

                if rule["response"] == "TIME_FEATURE":
                    return f"⏰ Current Time: {datetime.now().strftime('%H:%M:%S')}"

                if rule["response"] == "DATE_FEATURE":
                    return f"📅 Today's Date: {datetime.now().strftime('%Y-%m-%d')}"

                return rule["response"]

    # 2️⃣ Knowledge base matching
    for question, answer in knowledge_base.items():
        if question in user_input:
            return answer

    # 3️⃣ Smart fallback (any question)
    return random.choice(fallback_responses)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)