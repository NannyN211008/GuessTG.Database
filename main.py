from flask import Flask, render_template, request, session, redirect
import db

app = Flask(__name__)
app.secret_key = "gtg"

# Secure session cookies
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['SESSION_COOKIE_SECURE'] = False


@app.route("/")
def Home():
    guessData = db.GetAllGuesses()
    return render_template("index.html", guesses=guessData)


@app.route("/login", methods=["GET", "POST"])
def Login():

    # already logged in → redirect home
    if "id" in session:
        return redirect("/")

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

    # already logged in → redirect home
    if "id" in session:
        return redirect("/")

    error = None

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        success, message = db.RegisterUser(username, password)

        if success:
            return redirect("/login")
        else:
            error = message

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