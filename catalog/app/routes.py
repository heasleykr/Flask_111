#!/user/bin/env python3
# -*- coding: utf8 -*-
""" HTTP route definitions """

from flask import request
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime

@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S") # go back
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/products")
def get_all_products():
    out = scan()
    out["ok"] = True
    out["message"] = "Success"
    return out

@app.route("/products/<pid>")
def get_one_product(pid):
    out = read(int(pid))
    out["ok"] = True
    out["message"] = "Success"
    return out

@app.route("/products", methods=["POST"])
def create_product():
    product_data = request.json
    new_id = create(
        product_data.get("name"),
        product_data.get("price"),
        product_data.get("category"),
        product_data.get("description")
    )
    
    return {"ok": True, "message": "Success", "new_id": new_id}

@app.route("/products/<pid>", methods=["PUT"])
def update_product(pid):
    product_data = request.json
    out = update(int(pid), product_data)
    return {"ok": out, "message": "Updated"}

app.add_url_rule("/katelynn", "index", index)

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, %s!</h1>" % name

@app.route('/square/<int:number>')
def square(number):
    return ("<h1>%s squared is %s</h1>" % (number, number**2))

@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent