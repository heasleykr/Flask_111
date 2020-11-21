# !/user/bin/env python3
# -*- coding: utf8 -*-
"""A simple flask app """


# Import the Flask class from flask module


from flask import Flask


app = Flask(__name__)

from app import routes  # from app folder, import 'routes.py'
