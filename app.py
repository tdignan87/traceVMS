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

# constants
question_table = mongo.db.av_questions
contractor_table = mongo.db.contractors
visitor_table = mongo.db.visitors

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/admin_panel")
def admin():
    return render_template("admin.html")

"""
Find and display questions and contractors in dropdown choices.
"""
@app.route("/sign_in")
def signin():
    return render_template("signin.html",
                           av_questions=question_table.find(),
                           contractors=contractor_table.find())

"""
Administrator login page to access admin menu . Username is 'sysdba' and password is 'masterkey'
"""
@app.route("/admin_login",methods=['GET','POST'])
def adminlogin():
    if request.method == "POST":
        users = mongo.db.users
        login_user = users.find_one({"username": request.form["username"]})
        if login_user:
           if request.form ["password"] ==  login_user["password"]:
               
               return redirect(url_for("admin"))
           else:
               return redirect(url_for("login"))
            
        return render_template("login.html")
    return render_template("login.html")
            
"""
Add signed in visitor details to database.
"""
@app.route("/add_visitor",methods=['POST'])
def add_visitor():
    
    dateTimeObj = datetime.now()
    add_new_visitor = {"name": request.form.get("visitorName"),
                       "company":request.form.get("visitorCompany"),
                       "visiting":request.form.get("visitorRepresent"),
                       "entered_bakery":bool(request.form.get("gridRadios")),
                       "company_representative":request.form.get("companyRepresent"),
                       "sign_in_timestamp": dateTimeObj}
     
    mongo.db.visitors.insert_one(add_new_visitor)
    return render_template("main.html")

"""
Return edit visitor page with visitors and contractors dropdown populated.
"""
@app.route("/edit_visitor")
def edit_visitor():
    return render_template("edit-visitor.html",
                           visitors=visitor_table.find(),
                           contractors=contractor_table.find())
    
"""
Update visitors based on input from the edit visitors page.
"""
@app.route("/amend_visitor",methods=['POST'])
def amend_visitor():
    visitor_id = request.form.get("chooseName")
    update = visitor_table
    update.update_one ({"_id": ObjectId(visitor_id)},
                       {"$set":{
                            "company": request.form.get("visitorCompany"),
                            "visiting": request.form.get("editVisiting")
                       }})
    return redirect(url_for("admin"))
                                       
@app.route("/delete")
def delete():
    return render_template("delete-visitor.html",
                           visitors=visitor_table.find())                  

"""
Delete visitor from the system
"""
@app.route("/delete_visitor",methods=['POST'])
def delete_visitor():
    visitor_id = request.form.get("deleteName")
    visitor_table.remove({"_id": ObjectId(visitor_id)})
    return redirect(url_for("admin"))

@app.route("/add_company")
def addcompany():
    return render_template("add-company.html")

"""
Add new company details into DB
"""
@app.route("/insert_company", methods=['POST'])
def insert_company():
    company_doc = {"Name": request.form.get("newCompanyName"),
                   "Address": request.form.get("newCompanyAddress"),
                    "approved":request.form.get("approveRadios")}
    contractor_table.insert_one(company_doc)
    return redirect(url_for("admin"))

@app.route("/edit_company")
def edit_company():
    return render_template("edit-company.html",
                           contractors=mongo.db.contractors.find()) 
   
@app.route("/update_company",methods=['POST'])
def update_company():
    company_id = request.form.get("chooseCompany")
    update = contractor_table
    update.update_one({"_id": ObjectId(company_id)},
                      {"$set": {
                          "Address": request.form.get("editCompAddress"),
                          "approved": request.form.get("approveRadios")
                      }})
    return redirect(url_for("admin"))

@app.route("/delete_company")
def delete_company():
    return render_template("delete-company.html",
                           contractors=contractor_table.find())

@app.route("/delete_company_record",methods=['POST'])
def delete_company_record():
    company_id = request.form.get("deleteCompany")
    contractor_table.remove({'_id': ObjectId(company_id)})
    return redirect(url_for("admin"))   
    
@app.route("/insert_question")
def insert_question():
    return render_template("add-questions.html")

    """
    Add New Questions into DB
    """
@app.route("/add_question", methods=['POST'])
def add_question():
    add_new_question = {"Question": request.form.get("newQuestionAdd"),
                        "Answer_First": request.form.get("newAnswerAdd"),
                        "Answer_Second": request.form.get("newAnswerAddSecond")}
    question_table.insert_one(add_new_question)
    return redirect(url_for("admin"))

@app.route("/sign_out")
def sign_out():
    return render_template("sign-out.html",
                           visitors=visitor_table.find())
    """
    Update visitor table by adding in signed out timestamp
    """
@app.route("/sign_out_visitor",methods=['POST'])
def sign_out_visitor():
    visitor_id = request.form.get("signOutName")
    dateTimeObj = datetime.now()
    signout = visitor_table
    signout.update_one ({"_id": ObjectId(visitor_id)},
                           {"$set":{
        "sign_out_timestamp":dateTimeObj 
    }})
    return redirect(url_for("home"))
                    
@app.route("/edit_question")
def edit_question():
    return render_template("edit-question.html",
                           av_questions=question_table.find())

@app.route("/update_question",methods=['POST'])
def update_question():
    question_id = request.form.get("amendQuestion")
    update = question_table
    update.update_one({"_id": ObjectId(question_id)},
                      {"$set": {
                        "Question": request.form.get("editQuestionAdd"),
                        "Answer_First": request.form.get("editAnswerAdd"),
                        "Answer_Second": request.form.get("editAnswerAddSecond")  
                      }})
    return redirect(url_for("admin"))

@app.route("/delete_question")
def delete_question():
    return render_template("delete-question.html",
                           av_questions=question_table.find())

@app.route("/remove_question",methods=['POST'])
def remove_question():
    question_id = request.form.get("removeQuestion")
    question_table.remove({"_id": ObjectId(question_id)})
    return redirect(url_for("admin"))

"""
Get values from database for visitors and display on page for only signed in visitors
"""

@app.route("/dashboard_load",methods=['GET'])
def dash_load():
       visitors = visitor_table.find({},{"name":1,
                                        "sign_out_timestamp":1,
                                        "company":1})
       
       dateTime = datetime.now()
       return render_template("dashboard.html", visitors = visitors,
                              dateTime = dateTime)
                              
if __name__ == "__main__":
    app.run(debug=True)