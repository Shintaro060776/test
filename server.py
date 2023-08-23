from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

# OpenAI APIキーの設定
openai.api_key = "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"

app = Flask(__name__)

@app.route("/api/openai", methods=["POST"])
def openai_endpoint():
    prompt = request.json.get('prompt')
    data = request.json
    user_input = data.get("input")

    # OpenAIのAPIを叩く
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=user_input,
        max_tokens=150
    )

    return jsonify({"response": response.choices[0].text.strip()})
    # return jsonify(response_from_openai)

if __name__ == "__main__":
    app.run(debug=True)