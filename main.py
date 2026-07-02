from flask import Flask, render_template, request, session, redirect
from datetime import timedelta
import db

app = Flask(__name__)
app.secret_key = "gtg"

# -----------------------------
# Session Security Configuration
# -----------------------------
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False      # Change to True when using HTTPS
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)


@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)


@app.route("/login", methods=["GET", "POST"])
def Login():

    # Already logged in
    if "id" in session:
        return redirect("/")

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = db.CheckLogin(username, password)

        if user:

            # Prevent session fixation attacks
            session.clear()

            # Create a new secure session
            session.permanent = True
            session["id"] = user["id"]
            session["username"] = user["username"]

            return redirect("/")

        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/logout")
def Logout():

    # Destroy the user's session
    session.clear()

    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def Register():

    # Already logged in
    if "id" in session:
        return redirect("/")

    error = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        success, message = db.RegisterUser(username, password)

        if success:
            return redirect("/login")
        else:
            error = message

    return render_template("register.html", error=error)


@app.route("/add", methods=["GET", "POST"])
def Add():

    # Only fully authenticated users may access this page
 if "id" not in session or "username" not in session:
    session.clear()
    return redirect("/login")

    if request.method == "POST":

        user_id = session["id"]
        date = request.form["date"]
        game = request.form["game"]
        score = request.form["score"]

        db.AddGuess(user_id, date, game, score)

        return redirect("/")

    return render_template("add.html")


app.run(debug=True, port=5000)