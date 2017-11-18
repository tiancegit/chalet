#!/usr/bin/env python
# encoding: utf-8

from flask import Flask

# from chalet.views import blueprint_first


app = Flask(__name__)
app.config.from_object("chalet.config")

# register blueprint
# app.register_blueprint(blueprint_first, prefix='/first')



@app.before_request
def before_request():
    pass


@app.after_request
def after_request(resp):
    return resp


@app.errorhandler(404)
def page_not_found(err):
    return '404'
