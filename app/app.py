from flask import Flask
import urllib.request

app = Flask(__name__)

@app.route("/")
def home():
    backend_response = urllib.request.urlopen(
        "http://backend:5001"
    ).read().decode()

    return f"Platform received: {backend_response}"

app.run(host="0.0.0.0", port=5000)
