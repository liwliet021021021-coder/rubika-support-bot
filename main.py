from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

@app.route("/")
def home():
    webhook_url = "https://rubika-support-bot-production.up.railway.app/receiveUpdate"

    r = requests.post(
        f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/updateBotEndpoints",
        json={
            "url": webhook_url,
            "type": "ReceiveUpdate"
        },
        timeout=20
    )

    return {
        "status": "ok",
        "result": r.json()
    }

@app.route("/receiveUpdate", methods=["POST"])
def receive_update():
    data = request.json

    print("=" * 50)
    print(data)
    print("=" * 50)

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
