from flask import Flask, render_template, url_for, request, redirect, session
import os
import bcrypt
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask (__name__)
app.config["MONGO_DBNAME"] = "vms"
app.config["MONGO_URI"] = "mongodb+srv://root:P4Wnet95pal@myfirstcluster-8kwur.mongodb.net/vms?retryWrites=true&w=majority"

mongo = PyMongo(app)



@app.route("/")
def home():
    return render_template("base.html")

@app.route("/admin_panel")
def admin():
    return render_template("admin.html")

@app.route("/sign_in")
def signin():
    return render_template("signin.html")

@app.route("/admin_login")
def adminlogin():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)