import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

def GetDB():

    # Connect to the database and return the connection object
    db = sqlite3.connect(".database/gtg.db")
    db.row_factory = sqlite3.Row

    return db


def GetAllGuesses():

    # Connect, query all guesses and then return the data
    db = GetDB()
    guesses = db.execute("SELECT * FROM Guesses").fetchall()
    db.close()

    return guesses


##################################
### New code starts here
##################################

def CheckLogin(username, password):

    db = GetDB()

    # Ask the database for a single user matching the provided name
    user = db.execute(
        "SELECT * FROM Users WHERE username=?",
        (username,)
    ).fetchone()

    db.close()

    # Do they exist?
    if user is not None:

        # Is their password correct?
        if check_password_hash(user['password'], password):

            # Login successful
            return user

    # Login failed
    return None

def ResetPassword(username, new_password):
    
    db = GetDB()

    hashed = generate_password_hash(new_password)

    db.execute(
        "UPDATE Users SET password=? WHERE username=?",
        (hashed, username)
    )

    db.commit()
    db.close()