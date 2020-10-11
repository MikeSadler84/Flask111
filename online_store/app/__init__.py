#!/usr/bin/env python3

"""Basic Flask Program"""


from flask import Flask

app = Flask(__name__)

from app import routes