from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Rubika Support Bot Online"

@app.route("/receiveUpdate", methods=["POST"])
def update():
    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
