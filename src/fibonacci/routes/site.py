from flask import Blueprint, render_template

mod = Blueprint("site", __name__)


@mod.route("/")
def home():
    return render_template("home.html")
