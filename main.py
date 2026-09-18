from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")


def send_message(chat_id, text):

    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    try:
        r = requests.post(url, json=payload, timeout=20)

        print("STATUS:", r.status_code)
        print("RESPONSE:", r.text)

        return r.json()

    except Exception as e:
        print("SEND ERROR:", e)
        return None


@app.route("/")
def home():
    return "ONLINE"


@app.route("/receiveUpdate", methods=["POST"])
def receive_update():

    data = request.json

    print("=" * 50)
    print(data)
    print("=" * 50)

    try:

        update = data.get("update", {})

        if update.get("type") == "NewMessage":

            chat_id = update.get("chat_id")

            message = update.get("new_message", {})

            text = message.get("text", "")

            print("CHAT:", chat_id)
            print("TEXT:", text)

            if text == "/start":

                send_message(
                    chat_id,
                    "سلام 👋\nربات با موفقیت فعال است."
                )

            elif text:

                send_message(
                    chat_id,
                    f"پیام شما دریافت شد:\n{text}"
                )

        return {"ok": True}

    except Exception as e:

        print("ERROR:", e)

        return {
            "ok": False,
            "error": str(e)
        }


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )
