from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# تنظیمات
# =========================

ADMIN_GROUP_ID = "g0IZ3is000677376b8e6cfd1eec21a99"

# =========================
# ارسال پیام
# =========================

def send_message(print(data)):

    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    if chat_keypad:
        data["chat_keypad_type"] = "New"
        data["chat_keypad"] = chat_keypad

    if inline_keypad:
        data["inline_keypad"] = inline_keypad

    try:

        response = requests.post(
            url,
            json=data,
            timeout=20
        )

        print("SEND MESSAGE STATUS:", response.status_code)
        print("SEND MESSAGE RESPONSE:", response.text)

        return response.json()

    except Exception as e:

        print("SEND MESSAGE ERROR:", e)
        return None


# =========================
# منوی اصلی
# =========================

from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# تنظیمات
# =========================

ADMIN_GROUP_ID = "g0IZ3is000677376b8e6cfd1eec21a99"

# =========================
# ارسال پیام
# =========================

def send_message(chat_id, text, chat_keypad=None, inline_keypad=None):

    url = f"https://botapi.rubika.ir/v3/{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    if chat_keypad:
        data["chat_keypad_type"] = "New"
        data["chat_keypad"] = chat_keypad

    if inline_keypad:
        data["inline_keypad"] = inline_keypad

    try:

        response = requests.post(
            url,
            json=data,
            timeout=20
        )

        print("SEND MESSAGE STATUS:", response.status_code)
        print("SEND MESSAGE RESPONSE:", response.text)

        return response.json()

    except Exception as e:

        print("SEND MESSAGE ERROR:", e)
        return None


# =========================
# منوی اصلی
# =========================

def handle_start(chat_id):

    send_message(
        chat_id,
        "ربات روشن است ✅"
    )

# =========================
# شروع ربات
# =========================

def handle_start(chat_id):

    main_menu(chat_id)


# =========================
# دریافت آپدیت
# =========================

@app.route("/receiveUpdate", methods=["POST"])
def receive_update():

    data = request.json

    print("=" * 50)
    print("NEW UPDATE:")
    print(data)
    print("=" * 50)

    try:

        update = data.get("update", {})

        update_type = update.get("type")

        if update_type == "NewMessage":

            chat_id = update.get("chat_id")

            new_message = update.get("new_message", {})

            text = new_message.get("text", "")
            aux_data = update.get("aux_data", {})

            print("CHAT ID:", chat_id)
            print("TEXT:", text)
            print("AUX DATA:", aux_data)

            # =========================
            # /start
            # =========================

            if text == "/start":

                handle_start(chat_id)

            # =========================
            # پشتیبانی
            # =========================

            elif text == "🎫 پشتیبانی":

                send_message(
                    chat_id,
                    "🎫 بخش پشتیبانی\n\n📝 موضوع خود را مطرح کنید."
                )

            # =========================
            # گزارش تخلف
            # =========================

            elif text == "🚨 گزارش تخلف":

                send_message(
                    chat_id,
                    "🚨 بخش گزارش تخلف\n\n👤 لطفاً اسم فرد متخلف را ارسال کنید."
                )

            # =========================
            # عضوگیری
            # =========================

            elif text == "👥 درخواست عضوگیری":

                send_message(
                    chat_id,
                    "👥 درخواست عضوگیری\n\nبرای شروع درخواست عضویت، قوانین کلن را مطالعه کنید."
                )

            # =========================
            # دکمه های دارای ID
            # =========================

            button_id = aux_data.get("button_id")

            if button_id:

                print("BUTTON ID:", button_id)

                if button_id == "support":

                    send_message(
                        chat_id,
                        "🎫 بخش پشتیبانی\n\n📝 موضوع خود را مطرح کنید."
                    )

                elif button_id == "report":

                    send_message(
                        chat_id,
                        "🚨 بخش گزارش تخلف\n\n👤 لطفاً اسم فرد متخلف را ارسال کنید."
                    )

                elif button_id == "recruitment":

                    send_message(
                        chat_id,
                        "👥 درخواست عضوگیری\n\nبرای شروع درخواست عضویت، قوانین کلن را مطالعه کنید."
                    )

        return {"ok": True}

    except Exception as e:

        print("UPDATE ERROR:", e)

        return {
            "ok": False,
            "error": str(e)
        }


# =========================
# صفحه تست
# =========================

@app.route("/")
def home():
    return "ONLINE"


# =========================
# اجرا
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )


# =========================
# شروع ربات
# =========================

def handle_start(chat_id):

    main_menu(chat_id)


# =========================
# دریافت آپدیت
# =========================

@app.route("/receiveUpdate", methods=["POST"])
def receive_update():

    data = request.json

    print("=" * 50)
    print("NEW UPDATE:")
    print(data)
    print("=" * 50)

    try:

        update = data.get("update", {})

        update_type = update.get("type")

        if update_type == "NewMessage":

            chat_id = update.get("chat_id")

            new_message = update.get("new_message", {})

            text = new_message.get("text", "")
            aux_data = update.get("aux_data", {})

            print("CHAT ID:", chat_id)
            print("TEXT:", text)
            print("AUX DATA:", aux_data)

            # =========================
            # /start
            # =========================

            if text == "/start":

                handle_start(chat_id)

            # =========================
            # پشتیبانی
            # =========================

            elif text == "🎫 پشتیبانی":

                send_message(
                    chat_id,
                    "🎫 بخش پشتیبانی\n\n📝 موضوع خود را مطرح کنید."
                )

            # =========================
            # گزارش تخلف
            # =========================

            elif text == "🚨 گزارش تخلف":

                send_message(
                    chat_id,
                    "🚨 بخش گزارش تخلف\n\n👤 لطفاً اسم فرد متخلف را ارسال کنید."
                )

            # =========================
            # عضوگیری
            # =========================

            elif text == "👥 درخواست عضوگیری":

                send_message(
                    chat_id,
                    "👥 درخواست عضوگیری\n\nبرای شروع درخواست عضویت، قوانین کلن را مطالعه کنید."
                )

            # =========================
            # دکمه های دارای ID
            # =========================

            button_id = aux_data.get("button_id")

            if button_id:

                print("BUTTON ID:", button_id)

                if button_id == "support":

                    send_message(
                        chat_id,
                        "🎫 بخش پشتیبانی\n\n📝 موضوع خود را مطرح کنید."
                    )

                elif button_id == "report":

                    send_message(
                        chat_id,
                        "🚨 بخش گزارش تخلف\n\n👤 لطفاً اسم فرد متخلف را ارسال کنید."
                    )

                elif button_id == "recruitment":

                    send_message(
                        chat_id,
                        "👥 درخواست عضوگیری\n\nبرای شروع درخواست عضویت، قوانین کلن را مطالعه کنید."
                    )

        return {"ok": True}

    except Exception as e:

        print("UPDATE ERROR:", e)

        return {
            "ok": False,
            "error": str(e)
        }


# =========================
# صفحه تست
# =========================

@app.route("/")
def home():
    return "ONLINE"


# =========================
# اجرا
# =========================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=8080
    )
