#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Product Form """


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField("What is the product's name?", validators=[DataRequired()])
    price = StringField("How much will it cost?", validators=[DataRequired()])
    category = StringField("What is the product's category?", validators=[DataRequired()])
    description = StringField("Enter a description", validators=[DataRequired()])
    submit = SubmitField("Submit")