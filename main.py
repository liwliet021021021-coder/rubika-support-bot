from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# Send Message
# =========================

def send_message(chat_id, text, keypad=None):

    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    if keypad:
        payload["chat_keypad_type"] = "New"
        payload["chat_keypad"] = keypad

    print("SEND DATA:", payload)

    try:

        r = requests.post(
            url,
            json=payload,
            timeout=20
        )

        print("STATUS:", r.status_code)
        print("RESPONSE:", r.text)

        return r.json()

    except Exception as e:

        print("SEND ERROR:", e)
        return None


# =========================
# Main Menu
# =========================

def show_main_menu(chat_id):

    keypad = {
        "rows": [
            {
                "buttons": [
                    {
                        "id": "support",
                        "type": "Simple",
                        "button_text": "🎫 پشتیبانی"
                    },
                    {
                        "id": "report",
                        "type": "Simple",
                        "button_text": "🚨 گزارش تخلف"
                    }
                ]
            },
            {
                "buttons": [
                    {
                        "id": "recruitment",
                        "type": "Simple",
                        "button_text": "👥 درخواست عضوگیری"
                    }
                ]
            }
        ],
        "resize_keyboard": True,
        "on_time_keyboard": False
    }

    send_message(
        chat_id,
        "🐺 به ربات DISCORT_WOLFS خوش آمدید\n\nیکی از گزینه‌ها را انتخاب کنید:",
        keypad
    )


# =========================
# Webhook
# =========================

@app.route("/receiveUpdate", methods=["POST"])
def receive_update():

    data = request.json

    print("=" * 50)
    print(data)
    print("=" * 50)

    try:

        update = data.get("update", {})

        if update.get("type") != "NewMessage":
            return {"ok": True}

        chat_id = update.get("chat_id")

        message = update.get("new_message", {})

        text = message.get("text", "")

        aux_data = update.get("aux_data", {})

        print("CHAT:", chat_id)
        print("TEXT:", text)
        print("AUX:", aux_data)

        # start command

        if text == "/start":

            show_main_menu(chat_id)

            return {"ok": True}

        # button click

        button_id = aux_data.get("button_id")

        if button_id == "support":

            send_message(
                chat_id,
                "🎫 بخش پشتیبانی\n\nپیام خود را ارسال کنید."
            )

        elif button_id == "report":

            send_message(
                chat_id,
                "🚨 بخش گزارش تخلف\n\nاطلاعات تخلف را ارسال کنید."
            )

        elif button_id == "recruitment":

            send_message(
                chat_id,
                "👥 درخواست عضوگیری\n\nدرخواست خود را ارسال کنید."
            )

        return {"ok": True}

    except Exception as e:

        print("ERROR:", e)

        return {
            "ok": False,
            "error": str(e)
        }


@app.route("/")
def home():

    return "ONLINE"


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )
