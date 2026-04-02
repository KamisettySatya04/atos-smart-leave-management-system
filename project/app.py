from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user (for now)
USERNAME = "admin"
PASSWORD = "admin123"

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("home"))
    else:
        return "Invalid Credentials"

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)