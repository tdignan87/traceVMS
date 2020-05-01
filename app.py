from flask import Flask, render_template, url_for, request, redirect, session
import os
import bcrypt
from flask_pymongo import PyMongo
from datetime import datetime
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
    return render_template("signin.html",
                           av_questions=mongo.db.av_questions.find(),
                           contractors=mongo.db.contractors.find())

@app.route("/admin_login",methods=['GET','POST'])
def adminlogin():
    users = mongo.db.users
    error = None
    if request.method == "POST":
        if request.form["username"] == users.username or request.form["password"] == users.password:
            error = "Invalid Credentials, please try again"
        else:
            return redirect(url_for("admin"))
    return render_template("login.html", error=error)
    

@app.route("/add_visitor",methods=['POST'])
def add_visitor():
    dateTimeObj = datetime.now()
    add_new_visitor = {"name": request.form.get("visitorName"),
                       "company":request.form.get("visitorCompany"),
                       "visiting":request.form.get("visitorRepresent"),
                       "entered_bakery":request.form.get("gridRadios"),
                       "company_representative":request.form.get("companyRepresent"),
                       "sign_in_timestamp": dateTimeObj}
    mongo.db.visitors.insert_one(add_new_visitor)
    return render_template("main.html")

@app.route("/add_company")
def addcompany():
    return render_template("add-company.html")

@app.route("/insert_company", methods=['POST'])
def insert_company():
    company_doc = {"Name": request.form.get("newCompanyName"),
                   "Address": request.form.get("newCompanyAddress"),
                    "approved":request.form.get("approveRadios")}
    mongo.db.contractors.insert_one(company_doc)
    return redirect(url_for("admin"))
    
@app.route("/insert_question")
def insert_question():
    return render_template("add-questions.html")
    
@app.route("/add_question", methods=['POST'])
def add_question():
    add_new_question = {"Question": request.form.get("newQuestionAdd"),
                        "Answer_First": request.form.get("newAnswerAdd"),
                        "Answer_Second": request.form.get("newAnswerAddSecond")}
    mongo.db.av_questions.insert_one(add_new_question)
    return redirect(url_for("admin"))

@app.route("/sign_out")
def sign_out():
    return render_template("sign-out.html",
                           visitors=mongo.db.visitors.find())
    
@app.route("/sign_out_visitor",methods=['POST'])
def sign_out_visitor():
    visitor_id = request.form.get("signOutName")
    dateTimeObj = datetime.now()
    signout = mongo.db.visitors
    signout.update_one ({"_id": ObjectId(visitor_id)},
                           {"$set":{
        "sign_out_timestamp":dateTimeObj 
    }})
    return redirect(url_for("home"))
                    

if __name__ == "__main__":
    app.run(debug=True)