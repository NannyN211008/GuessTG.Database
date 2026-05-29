import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def GetDB():
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row
    return db


def GetAllGuesses():
    db = GetDB()
    guesses = db.execute("SELECT * FROM Guesses").fetchall()
    db.close()
    return guesses


def CheckLogin(username, password):

    db = GetDB()

    user = db.execute(
        "SELECT * FROM Users WHERE username=?",
        (username,)
    ).fetchone()

    db.close()

    if user and check_password_hash(user['password'], password):
        return user

    return None


def RegisterUser(username, password):

    if not username or not password:
        return False

    db = GetDB()

    existing = db.execute(
        "SELECT * FROM Users WHERE username=?",
        (username,)
    ).fetchone()

    if existing:
        db.close()
        return False

    hashed = generate_password_hash(password)

    db.execute(
        "INSERT INTO Users(username, password) VALUES(?, ?)",
        (username, hashed)
    )

    db.commit()
    db.close()

    return True


def ResetPassword(username, new_password):

    db = GetDB()

    user = db.execute(
        "SELECT * FROM Users WHERE username=?",
        (username,)
    ).fetchone()

    if not user:
        db.close()
        return False

    hashed = generate_password_hash(new_password)

    db.execute(
        "UPDATE Users SET password=? WHERE username=?",
        (hashed, username)
    )

    db.commit()
    db.close()

    return True


# ✅ ADD THIS (STEP 12 REQUIREMENT)
def AddGuess(user_id, date, game, score):

    if not date or not game:
        return False

    db = GetDB()

    db.execute(
        "INSERT INTO Guesses(user_id, date, game, score) VALUES (?, ?, ?, ?)",
        (user_id, date, game, score)
    )

    db.commit()
    db.close()

    return True