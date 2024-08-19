from flask import Flask, render_template
import datetime
import requests
import json

app = Flask(__name__)


@app.route("/")
def start_screen():
    return "Hello User Welcome to the Site"

@app.route("/guess/<vname>")
def guess_name(vname):
    gender_url = f"https://api.genderize.io?name={vname}"
    age_url = f"https://api.agify.io?name={vname}"
    result = requests.get(gender_url)
    r = requests.get(age_url)
    r_age = r.json()
    result_info = result.json()
    p_age = r_age["age"]
    p_gender = result_info["gender"]
    return render_template("index.html",person_name = vname, age=p_age, gender=p_gender)

@app.route("/blogs")
def blogs_posted():
    res = requests.get("https://api.npoint.io/685c852ac3a06729360e")
    post = res.json()
    all_post = post["blogs"]
    return render_template("blogs.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)
