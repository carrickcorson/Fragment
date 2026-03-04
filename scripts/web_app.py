from flask import (Flask,
                   Response,
                   request,
                   jsonify,
                   render_template,
                   stream_with_context)
from pipeline import Pipeline
import json
from collections.abc import Generator

app = Flask(__name__)
pipe = Pipeline()

def generate(
        messages: list
    ) -> Generator[str, None, None]:
    
    for chunk in pipe.chat(messages):
        yield f"data: {json.dumps({'chunk': chunk})}\n\n"
    yield "data: [DONE]\n\n"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data["messages"]

    return Response(stream_with_context(generate(messages)), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
