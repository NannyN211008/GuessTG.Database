import sqlite3
import re
from werkzeug.security import generate_password_hash, check_password_hash


def GetDB():
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row
    return db


def GetAllGuesses():

    db = GetDB()

    guesses = db.execute("""
        SELECT Guesses.date, Guesses.game, Guesses.score, Users.username
        FROM Guesses
        JOIN Users ON Guesses.user_id = Users.id
        ORDER BY Guesses.date DESC
    """).fetchall()

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
    
    # Check username and password are entered
    if not username or not password:
        return False, "Username and password cannot be empty."

    # Username validation
    if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
        return False, "Username must be 3-20 characters and contain only letters, numbers or underscores."

    # Password validation
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)

    if not (has_upper and has_lower and has_digit):
        return False, "Password must contain an uppercase letter, lowercase letter and a number."

    db = GetDB()

    existing = db.execute(
        "SELECT * FROM Users WHERE username=?",
        (username,)
    ).fetchone()

    if existing:
        db.close()
        return False, "Username already exists."

    hashed = generate_password_hash(password)

    db.execute(
        "INSERT INTO Users(username, password) VALUES(?, ?)",
        (username, hashed)
    )

    db.commit()
    db.close()

    return True, None


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


def AddGuess(user_id, date, game, score):
    
    # Validate inputs
    if not date or not game:
        return False

    # Limit game name length
    if len(game) > 100:
        return False

    # Remove leading/trailing spaces
    game = game.strip()

    # Validate score
    try:
        score = int(score)
    except ValueError:
        return False

    if score < 0 or score > 6:
        return False

    db = GetDB()

    db.execute(
        "INSERT INTO Guesses(user_id, date, game, score) VALUES (?, ?, ?, ?)",
        (user_id, date, game, score)
    )

    db.commit()
    db.close()

    return True