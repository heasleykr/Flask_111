#!/user/bin/env python3
# -*- coding: utf8 -*-
"""Routes file: specifices http routes """


# from app Module, import the app variable in __init__.py module
from flask import g  # object for storing data during runtime
from app import app
import sqlite3  # your relational database management system (RDMS)

DATABASE = "/Users/KatelynnHeasley/Desktop/SDGKU/flask_111/my_page.db"


def get_db():
    # get DB attr IF it exists, if not, return NONE
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def return_users():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
    return db # may be an error. 


# specify the route.
# the decorator is mapping the route to the forward fn.
# .route is the decorator
@app.route("/")
def index():
    return "Hello, world!"

# this is returned as a JSON.
@app.route("/aboutme")
def aboutme():
    return '''
    <html>
       <head>
         <title>About Me</title>
       </head>
        <body>
        <h1>About The Developer</h1>
        <p>first_name: Katelynn</p>
        <p>last-Name: Heasley</p>
        <p>Hobby: Learning to Code!</p>
        </body>
    </html>
    '''

@app.route("/users")
def dump_json():
    out = {"ok": True, "body": ""} 
    users = return_users() #grab DB results, which are formatted in tuples

    body_list = [] #create list to hold JSON formatted DB results

    #loop through tuple DB results and convert to dictionary format (key/value data type)
    for user in users:
        temp_dictionary = {} #create dictionary
        temp_dictionary["first_name"] = user[0] #add key/value elements to dictionary
        temp_dictionary["last_name"] = user[1]
        temp_dictionary["hobbies"] = user[2]
        body_list.append(temp_dictionary)
    
    out["body"] = body_list #add JSON dictionary results to your Out Dictionary to return
    
    return out
