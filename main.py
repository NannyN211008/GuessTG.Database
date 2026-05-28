from flask import Flask, render_template, request
import db

app = Flask(__name__)
app.secret_key = "gtg"

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)