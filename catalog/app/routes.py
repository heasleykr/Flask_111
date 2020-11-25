#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" HTTP route definitions """

from flask import request, render_template #allows interations with any requests. #renders our templates!
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime
from app.forms.product import ProductForm



@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S") # verify server time. Used for users to verify if server is running
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/product_form", methods=["GET", "POST"])
def product_form():
    if request.method == "POST":
        p_Name = request.form.get("name")
        p_Price = request.form.get("price")
        p_Category = request.form.get("category")
        p_Description = request.form.get("description")

        create(p_Name, p_Price, p_Category, p_Description)
        
    form = ProductForm()

    return render_template("form_example.html", form=form)

@app.route("/products")
def get_all_products():
    out = scan() 
    out["ok"] = True
    out["message"] = "Success"
    # return out
    return render_template("products.html", products=out["body"])

@app.route("/products/<pid>")#pid is product id when we have them
def get_one_product(pid):
    out = read(int(pid)) #read incomming product, format as an integer
    out["ok"] = True
    out["message"] = "Success"
    return out

#method to create a new product and add to db
#you can add multiple request methods as params if you need. Not recommended.
@app.route("/products", methods=["POST"])
def create_product():
    product_data = request.json
    new_id = create(
        product_data.get("name"), #find the key "name" and set value
        product_data.get("price"),
        product_data.get("category"),
        product_data.get("description")
    )
    #this is returned as a JSON first, then converted to a python dictionary
    return {"ok": True, "message": "Success", "new_id": new_id}

@app.route("/products/<pid>", methods=["PUT"])
def update_product(pid):
    product_data = request.json
    out = update(int(pid), product_data)
    return {"ok": out, "message": "Updated"}

#Example of routing w/o the Flask '@app.route'. 
app.add_url_rule("/katelynn", "index", index)

#the term is a 'View Route' because it returns HTML content
@app.route('/user/<name>')
#param is the user content to be added to the string output view. '%' dynamic content 
def user(name):
    last_name="Heasley"
    hobbies="Hiking"
    return render_template("about_me.html", first_name=name, last_name=last_name, hobbies=hobbies)

#this user input is cast directly into an int automatically <int:number>
#'number**2' - this is a python shortcut for squaring a number
@app.route('/square/<int:number>')
def square(number):
    return ("<h1>%s squared is %s</h1>" % (number, number**2))

#This prints out the User-Agent for your web browser!
@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent

#our error 404 html page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
