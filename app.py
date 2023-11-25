from flask import Flask, render_template, request
import json
import os.path
from utils import *


app = Flask(__name__)

@app.route('/')
def index() :
    dict = home()
    return render_template("index.html", dict = dict)

@app.route('/articles/<page>')
def article(page) :
    path = os.path.join("templates", "articles",page)
    isfile = os.path.isfile(path)
    if isfile == False :
        return 'No such File'
    return render_template(os.path.join("articles/", page))

@app.route('/related/<topic>')
def related(topic) :
    related = related_articles(topic, 10)
    return render_template("related.html" ,related=related)

@app.route("/a/<topic>") 
def topic(topic) : 
    dict = related_articles(topic, 20)
    return render_template("explore.html", dict=dict, topic=topic)

@app.route("/search",methods = ['POST','GET']) 
def search() : 
    q = request.args.get("q")
    dict = search_matches(q, 30)
    if len(dict) == 0 :
        return "SORRY , NO MATCHES"

    return render_template("search.html", dict = dict, topic = q)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

