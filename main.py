from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "gtg"


@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)


@app.route("/login", methods=["GET", "POST"])
def Login():

    error = None

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        user = db.CheckLogin(username, password)

        if user:
            session['id'] = user['id']
            session['username'] = user['username']
            return redirect("/")
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


@app.route("/logout")
def Logout():
    session.clear()
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def Register():

    error = None

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        if db.RegisterUser(username, password):
            return redirect("/")
        else:
            error = "Username already exists or invalid input"

    return render_template("register.html", error=error)


@app.route("/add", methods=["GET", "POST"])
def Add():

    # must be logged in
    if "id" not in session:
        return redirect("/login")

    if request.method == "POST":
        user_id = session['id']
        date = request.form['date']
        game = request.form['game']
        score = request.form['score']

        db.AddGuess(user_id, date, game, score)

        return redirect("/")

    return render_template("add.html")


app.run(debug=True, port=5000)