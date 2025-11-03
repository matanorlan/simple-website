from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    name = os.getenv("SITE_NAME", "Simple Website")
    return render_template("index.html", name=name)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/version")
def version():
    v = os.getenv("APP_VERSION")
    if not v:
        try:
            with open("VERSION", "r") as f:
                v = f.read().strip()
        except FileNotFoundError:
            v = "0.0.0-dev"
    return jsonify(version=v)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
