#!/usr/bin/env python3

"""Flask Routes: specifies http routes"""
from app import app

@app.route('/')
    
def my_dict():
    me_dict = {
        "First Name": "Mike",
        "Last Name": "Sadler",
        "Hobbies": ["Gaming", "Exercise", "Music"]
    }
    return me_dict