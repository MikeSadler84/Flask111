#!/usr/bin/env python3

"""Flask Routes: specifies http routes"""
from app import app

@app.route('/')

def index():
    return "Hello, World!"

    
