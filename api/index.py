import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from password_utils import evaluate_password

app = Flask(__name__, static_folder="../static", template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    entropy = None
    password = ""

    if request.method == "POST":
        password = request.form["password"]
        result, entropy = evaluate_password(password)

    return render_template("index.html", result=result, entropy=entropy, password=password)

# For Vercel deployment
def handler(environ, start_response):
    return app(environ, start_response)

# For local testing
if __name__ == "__main__":
    app.run(debug=True)
