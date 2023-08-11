from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import *

app = Flask(__name__)

app.config["SECRET_KEY"] = "IAMBATMAN"
debug = DebugToolbarExtension(app)

ans = {}

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}.""",
)


@app.route("/")
def home_page():
    """Home page containing the Madlibs form"""
    return render_template("home.html")


@app.route("/story")
def get_greeting():
    """Reuturns a story from the Madlibs form"""
    ans["place"] = request.args["place"]
    ans["noun"] = request.args["noun"]
    ans["verb"] = request.args["verb"]
    ans["adjective"] = request.args["adjective"]
    ans["plural_noun"] = request.args["plural_noun"]

    text = story.generate(ans)

    return render_template("story.html", text=text)
