from flask import Flask, render_template, url_for, request, redirect, session
import os
import bcrypt
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask (__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)



@app.route("/")
def home():
    return render_template("main.html")

@app.route("/admin_panel")
def admin():
    return render_template("admin.html")

@app.route("/sign_in")
def signin():
    return render_template("signin.html")

@app.route("/admin_login")
def adminlogin():
    return render_template("login.html")

@app.route("/add_visitor",methods=['POST'])
def add_visitor():
    add_new_visitor = {"name": request.form.get("visitorName"),
                       "company":request.form.get("visitorCompany"),
                       "visiting":request.form.get("visitorRepresent")}
    mongo.db.visitors.insert_one(add_new_visitor)
    return render_template("main.html")



if __name__ == "__main__":
    app.run(debug=True)