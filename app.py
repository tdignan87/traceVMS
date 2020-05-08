import os
from flask import Flask, render_template, url_for, request, redirect, flash,  session
import bcrypt
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask (__name__)
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

MONGO = PyMongo(app)

# constants
question_table = MONGO.db.av_questions
contractor_table = MONGO.db.contractors
visitor_table = MONGO.db.visitors
users_table = MONGO.db.users


@app.route("/")
def home():
    """Renders page that user will see on first load."""
    return render_template("pages/main.html")

@app.route("/admin/panel")
def admin():
    """Renders admin page after successful login."""
    return render_template("pages/admin.html")

@app.route("/signin/visitor",methods=['GET','POST'])
def signin():
    """
    Loads the sign in page and populates the dropdown fields from DB.
    Find and display questions and contractors in dropdown choices. POSTS data to database once saved.
    """
    if request.method == "POST":
        dateTimeObj = datetime.now()
        add_new_visitor = {"name": request.form.get("visitorName"),
                       "company":request.form.get("visitorCompany"),
                       "visiting":request.form.get("visitorRepresent"),
                       "entered_bakery":bool(request.form.get("gridRadios")),
                       "company_representative":request.form.get("companyRepresent"),
                       "sign_in_timestamp": dateTimeObj}
        visitor_table.insert_one(add_new_visitor)
        return render_template("pages/main.html")
    else:
        return render_template("pages/signin.html",
                           av_questions=question_table.find(),
                           contractors=contractor_table.find())
        
        
@app.route("/edit/visitor",methods=['GET','POST'])
def edit_visitor():
    """Renders page for editing visitors detail and posts changes back to the database."""    
    if request.method == "POST":
        visitor_id = request.form.get("chooseName")
        update = visitor_table
        update.update_one ({"_id": ObjectId(visitor_id)},
                       {"$set":{
                            "company": request.form.get("visitorCompany"),
                            "visiting": request.form.get("editVisiting")
                       }})
        return redirect(url_for("admin"))
    else:
        return render_template("pages/edit-visitor.html",
                           visitors=visitor_table.find(),
                           contractors=contractor_table.find())
    
@app.route("/delete/visitor",methods=['GET','POST'])
def delete_visitor():
    """ Renders delete page and allows deletion of visitor record """
    if request.method == "POST":
        visitor_id = request.form.get("deleteName")
        visitor_table.remove({"_id": ObjectId(visitor_id)})
        return redirect(url_for("admin"))
    else:
        return render_template("pages/delete-visitor.html",
                           visitors=visitor_table.find()) 
        

@app.route("/admin/login",methods=['GET','POST'])
def adminlogin():
    """ Admin render page, if correct credentials are entered page will load the admin panel to allow CRUD."""
    if request.method == "POST":
        users = users_table
        login_user = users.find_one({"username": request.form["username"]})
        if login_user:
           if request.form ["password"] ==  login_user["password"]:
               
               
               return redirect(url_for("admin"))
           else:
               flash("Login failed please try again")
               return redirect(url_for("login"))
            
            
        return render_template("pages/login.html")
    return render_template("pages/login.html")
            
                              
@app.route("/insert/new/company",methods=['GET','POST'])
def add_company():
    """ Renders page for inserting a new company and saves data into the database."""
    if request.method == "POST":
        company_doc = {"Name": request.form.get("newCompanyName"),
                   "Address": request.form.get("newCompanyAddress"),
                    "approved":bool(request.form.get("approveRadios"))}
        contractor_table.insert_one(company_doc)
        return redirect(url_for("admin"))
    else:
        return render_template("pages/add-company.html")

@app.route("/edit/company",methods=['GET','POST'])
def edit_company():
    """ Renders edit company page and saves amended data into the database."""
    if request.method == "POST":
        company_id = request.form.get("chooseCompany")
        update = contractor_table
        update.update_one({"_id": ObjectId(company_id)},
                      {"$set": {
                          "Address":request.form.get("editCompAddress"),
                          "approved":bool(request.form.get("approveRadios"))
                      }})
        return redirect(url_for("admin"))
    else:
        return render_template("pages/edit-company.html",
                           contractors=contractor_table.find()) 
   
@app.route("/delete/company",methods=['GET','POST'])
def delete_company():
    """ Renders delete company page and deletes record from database once submitted"""
    if request.method == "POST":
        company_id = request.form.get("deleteCompany")
        contractor_table.remove({'_id': ObjectId(company_id)})
        return redirect(url_for("admin"))
    else:
        return render_template("pages/delete-company.html",
                           contractors=contractor_table.find())


@app.route("/insert/question",methods=['GET','POST'])
def insert_question():
    """Renders insert questions page and saves new values into database """
    if request.method == "POST":
        add_new_question = {"Question": request.form.get("newQuestionAdd"),
                        "Answer_First": request.form.get("newAnswerAdd"),
                        "Answer_Second": request.form.get("newAnswerAddSecond")}
        question_table.insert_one(add_new_question)
        return redirect(url_for("admin"))
    else:
        return render_template("pages/add-questions.html")

                    
@app.route("/edit/question",methods=['GET','POST'])
def edit_question():
    """  edit questions page and saves updated values into database."""
    if request.method == "POST":
        question_id = request.form.get("amendQuestion")
        update = question_table
        update.update_one({"_id": ObjectId(question_id)},
                      {"$set": {
                        "Question": request.form.get("editQuestionAdd"),
                        "Answer_First": request.form.get("editAnswerAdd"),
                        "Answer_Second": request.form.get("editAnswerAddSecond")  
                      }})
        return redirect(url_for("admin"))
    else:
        return render_template("pages/edit-question.html",
                           av_questions=question_table.find())


@app.route("/delete/question",methods=['GET','POST'])
def delete_question():
    """ Renders delete question page and deletes question once submitted."""
    if request.method == "POST":
        question_id = request.form.get("removeQuestion")
        question_table.remove({"_id": ObjectId(question_id)})
        return redirect(url_for("admin"))
    else:
        return render_template("pages/delete-question.html",
                           av_questions=question_table.find())

""" Renders page that shows visitors on site based on db query."""
@app.route("/dashboard/load",methods=['GET'])
def dash_load():
       visitors = visitor_table.find({},{"name":1,
                                        "sign_out_timestamp":1,
                                        "company":1})
                                    
       dateTime = datetime.now()
       return render_template("pages/dashboard.html", visitors = visitors,
                              dateTime = dateTime)
                              
@app.route("/signout/visitor",methods=['GET','POST'])
def sign_out():
    """ Renders page for signing out visitor. Once visitor signs out a timestamp is added to DB """

    if request.method == "POST":
        visitor_id = request.form.get("signOutName")
        dateTimeObj = datetime.now()
        signout = visitor_table
        signout.update_one ({"_id": ObjectId(visitor_id)},
                           {"$set":{
        "sign_out_timestamp":dateTimeObj 
        }})
        return redirect(url_for("home"))
    else:
        return render_template("pages/sign-out.html",
                           visitors=visitor_table.find())
    
    
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)