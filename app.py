from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot logic
def chatbot_response(user_input):
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing fine!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(user_input.lower(), "Sorry, I don't understand that.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_reply = chatbot_response(user_message)
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
