import requests
from flask import Flask, render_template

app = Flask(__name__)
URL = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(URL)
data = response.json()


@app.route('/')
def home():
    return render_template('index.html', data=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/post/<int:blog_id>')
def single_blog(blog_id):
    return render_template("post.html", id=blog_id, posts=data)


if __name__ == "__main__":
    app.run(debug=True)
