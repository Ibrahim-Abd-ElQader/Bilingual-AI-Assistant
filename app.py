from flask import Flask, render_template, request, jsonify
from bot import get_response

app = Flask(__name__)

BOT_NAME = "AI Chatbot"

@app.route("/")
def home():
    
    return render_template("index.html", bot_name=BOT_NAME)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    
    app.run(debug=True, host="0.0.0.0", port=5000)
