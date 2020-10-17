#!/usr/bin/env python3

"""Flask Routes: specifies http routes"""
from flask import g, request, render_template
from app import app
import sqlite3

DATABASE = "online_store"

def get_db():
    db=getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def get_all_users():
    cursor = get_db().execute("SELECT * FROM user", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def update_user(to, string1, where, string2):
    cursor = get_db().execute("UPDATE user"  + to + "=" + string1 + " where " + where + "=" + string2 + ";")
    cursor.close()


def delete_user():
    cursor = get_db().execute("DELETE FROM user", ())
    cursor.close()


def create_user():
    cursor = get_db().execute("INSERT into user values", ("Michelangelo", "Turtle", "Skateboarding"))
    cursor.close()
   

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return "Hello, World!" 

@app.route('/aboutme')

def about_dict():
    me_dict = {
        "First Name": "Mike",
        "Last Name": "Sadler",
        "Hobbies": "Gaming"
    }
    return me_dict

@app.route("/countdown/<int:number>")

def countdown(number):
    return "</br>".join([ str(i) for i in range(number, 0, -1) ])
    
@app.route("/agent")
def agent():
    user_agent = request.header.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent

@app.route("/users", methods=["GET", "POST"])
def get_users():
    #creating an output dictionary
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        raw_data = get_all_users()
        for item in raw_data: 
           temp_dict = {"first_name": item[0], "last_name": item[1], "hobbies": item[2]}
           body_list.append(temp_dict)
        out["body"] = body_list
        return render_template(
            "base.html", 
            first_name=out["body"][0].get("first_name"), 
            last_name=out["body"][0].get("last_name"), 
            hobbies=out["body"][0].get("hobbies")
            )
    if "POST" in request.method:
        # create a new user
        create_user()
        
    if "PUT" in request.method:
        #update code goes here
        update_user()
        
    if "DELETE" in request.method:
        #update code goes here
        delete_user()
        pass