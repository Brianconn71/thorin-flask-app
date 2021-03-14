import os
import json
from flask import Flask, render_template

app = Flask(__name__)#instance of flask with the name of the applications module, flask needs this so it knows where to look in templates and static files

@app.route("/")# essentially, a way of wrapping functions
def index():
    return render_template("index.html")

@app.route("/about")#top level domain
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


#2 lines for pep8 compliance
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":#main is the default module in python
    app.run(
        use_debugger=True, 
        use_reloader=False, 
        passthrough_errors=True
    )
    #Do NOT have debug = True in projects or production code as it can allow arbitrary code to be run