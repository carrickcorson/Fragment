from flask import Flask, request, jsonify, render_template
from pipeline import Pipeline

app = Flask(__name__)
pipe = Pipeline()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data["messages"]
    response = pipe.chat(messages)

    return jsonify({"response": response})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
