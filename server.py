from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

DID_API_KEY = os.getenv("DID_API_KEY")  # Fetch API key from Railway

@app.route('/talks', methods=['POST'])
def generate_lip_sync():
    data = request.json
    text = data.get("text", "")

    response = requests.post(
        "https://api.d-id.com/talks",
        json={
            "source_url": "https://imgur.com/a/ai-generated-image-Fbqh9nv",
            "script": {"type": "text", "input": text}
        },
        headers={"Authorization": f"Bearer {DID_API_KEY}", "Content-Type": "application/json"}
    )

    return jsonify(response.json())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
