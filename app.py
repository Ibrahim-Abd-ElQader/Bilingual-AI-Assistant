# Flask web server for the AI Chatbot
# - Serves the chat interface (index.html)
# - Handles AJAX POST requests to get chatbot responses
from flask import Flask, render_template, request, jsonify
from bot import get_response

app = Flask(__name__)

# Optional: You can change the bot name displayed in the web interface
BOT_NAME = "AI Chatbot"

@app.route("/")
def home():
    # You can pass the bot name to the template if needed
    return render_template("index.html", bot_name=BOT_NAME)

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    reply = get_response(user_msg)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    # Run the app with debug mode enabled for development
    app.run(debug=True, host="0.0.0.0", port=5000)