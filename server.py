from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
from config import OPENAI_API_KEY

# OpenAI APIキーの設定
openai.api_key = OPENAI_API_KEY

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
        max_tokens=100,
        stop=None,  # 停止トークンの設定
        temperature=0.2,  # 生成時のランダム性の制御
        top_p=1,  # トークン選択時の確率閾値
    )

    return jsonify({"response": response.choices[0].text.strip()})
    # return jsonify(response_from_openai)

if __name__ == "__main__":
    app.run(debug=True)