from flask import Flask, request, render_template
from utils import load_data, get_post, show_comments, search_posts, get_user_feed, api_posts, api_post


app = Flask(__name__)
data = load_data()


@app.route("/")
def main_page():
    return render_template("index.html", data=data)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = get_post(post_id)
    comments = show_comments(post_id)
    return render_template("post.html", post=post, comments=comments)


@app.route("/search/")
def search_page():
    search_key = request.args.get("s")
    posts = search_posts(search_key)
    return render_template("search.html", posts=posts, search_key=search_key)


@app.route("/user-feed/<username>")
def user_feed(username):
    user_posts = get_user_feed(username)
    return render_template("user-feed.html", username=username, user_posts=user_posts)


@app.route("/api/posts/")
def get_posts_json():
    all_posts = api_posts()
    return f"<pre>{all_posts}</pre>"


@app.route("/api/posts/<int:post_id>")
def get_select_post(post_id):
    post = api_post(post_id)
    return f"<pre>{post}</pre>"


app.run(debug=True)
