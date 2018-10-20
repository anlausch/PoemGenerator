#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, redirect, url_for, Response
from logging.handlers import RotatingFileHandler
from time import strftime
import traceback
import logging
from flask_bootstrap import Bootstrap
from subprocess import Popen
import codecs


app = Flask(__name__)
Bootstrap(app)


@app.route('/get', methods=['POST'])
def create_poem():
    '''
    Returns a board with random letters to be rendered in the template
    '''
    try:
        p = Popen("translator.bat")
        poll = None
        while poll == None:
            poll = p.poll()
        with codecs.open("./de-poem.txt", "r", "utf-8", errors='ignore') as f:
            poem = f.read()
        return render_template("index.html", poem=poem)
    except Exception as e:
        return str(e)


@app.route('/', methods=['GET'])
@app.route('/get', methods=['GET'])
def index():
    return render_template("index.html")



@app.after_request
def after_request(response):
    """ Logging after every request. """
    # This avoids the duplication of registry in the log,
    # since that 500 is already logged via @app.errorhandler.
    if response.status_code != 500:
        ts = strftime('[%Y-%b-%d %H:%M]')
        logger.error('%s %s %s %s %s %s',
                      ts,
                      request.remote_addr,
                      request.method,
                      request.scheme,
                      request.full_path,
                      response.status)
    return response


@app.errorhandler(Exception)
def exceptions(e):
    """ Logging after every Exception. """
    ts = strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500


if __name__ == '__main__':
    print("Starting server")
    handler = RotatingFileHandler('./log/app.log', maxBytes=10000, backupCount=3)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    app.run(port=8000)