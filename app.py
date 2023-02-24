#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, session, render_template, Response
from  datetime import datetime
from secrets import token_hex
from pathlib import Path


static_folder = str(Path("./static").resolve())
template_folder = str(Path("./templates").resolve())

app = Flask('cell_counting', static_url_path='/static', template_folder=template_folder, static_folder=static_folder)
app.config['SECRET_KEY'] = token_hex(16)  # note: doing it like this means, that session dies between server restarts



# Image analysis 
@app.get("/")
@app.get("/index")
def index():
    session['uuid'] = "{:%Y-%m-%d_%H-%M-%S}_{}".format(datetime.now(), token_hex(8))
    return render_template("index.html")

@app.get("/about")
def about_me():
    return render_template("about.html")

@app.get("/contact")
def contact_info():
    return render_template("contact.html")



@app.get("/projects")
def my_tools():
    return render_template("projects.html")

if __name__ == "__main__":
    # Listen on all public IPs
    # https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
    app.run(host="0.0.0.0", port=5000)

# write in .bat "flask run --host=0.0.0.0"
