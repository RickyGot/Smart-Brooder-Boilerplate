from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for session and flash


# Load users from file into a dictionary
def load_users():
    users = {}
    with open("users.txt", "r") as f:
        for line in f:
            username, password = line.strip().split(":")
            users[username] = password
    return users


@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html", username=session["username"])
    else:
        flash("You need to log in first.")
        return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    users = load_users()
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username] == password:
            session["username"] = username
            flash("Login successful!")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password.")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully.")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True,port=5001)
