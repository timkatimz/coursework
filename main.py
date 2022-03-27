from flask import Flask, request, render_template
from utils import load_data, get_post, show_comments, search


app = Flask(__name__)
data = load_data()


@app.route("/")
def main_page():
    return render_template("index.html", data=data)


@app.route("/posts/<int:post_id>")         # не отображается значок глаза, неправильные пути
def show_post(post_id):
    post = get_post(post_id)
    comments = show_comments(post_id)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/")  # пока не работает
def search_by_name():
    search_key = request.args.get("search")
    posts = search(search_key)
    return render_template("search.html", posts=posts, search_key=search_key)

app.run(debug=True)