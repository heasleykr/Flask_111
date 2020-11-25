#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Simple database operations """
# """ Magic python file that tells python that it should be treated as a module """

from flask import Flask

app = Flask(__name__)

from app import routes