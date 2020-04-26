from flask import Flask, render_template, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask (__name__)

@app.route("/")
@app.route("/base")
def home():
    return render_template("base.html")

@app.route("/admin_panel")
def admin():
    return render_template("admin.html")




if __name__ == "__main__":
    app.run(debug=True)