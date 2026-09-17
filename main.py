from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

def send_message(chat_id, text):
    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text
        },
        timeout=20
    )

@app.route("/receiveUpdate", methods=["POST"])
def receive_update():
    data = request.json
    print(data)

    if data["update"]["type"] == "NewMessage":
        chat_id = data["update"]["chat_id"]

        if chat_id == "g0IZ3is000677376b8e6cfd1eec21a99":
def send_message(chat_id, text):
    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"

    r = requests.post(
        url,
        json={
            "chat_id": chat_id,
            "text": text
        },
        timeout=20
    )

    print(r.text)

    return {"ok": True}
@app.route("/")
def home():
    return "ONLINE"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
