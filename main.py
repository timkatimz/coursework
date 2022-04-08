from flask import Flask, request, render_template
from utils import load_data, get_post, show_comments, search_posts, get_user_feed, posts_by_tag, load_bookmarks
from api.views import api
from bookmarks.views import bookmarks

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(api)
app.register_blueprint(bookmarks)


@app.route("/")
def main_page():
    data = load_data()
    bookmarks_count = load_bookmarks()
    return render_template("index.html", data=data, bookmarks_count=bookmarks_count)


@app.route("/posts/<int:post_id>")
def show_post(post_id):
    post = get_post(post_id)
    comments = show_comments(post_id)
    return render_template("post.html", post=post, comments=comments, )


@app.route("/search/")
def search_page():
    search_key = request.args.get("s")
    posts = search_posts(search_key)
    return render_template("search.html", posts=posts, search_key=search_key)


@app.route("/user-feed/<username>")
def user_feed(username):
    user_posts = get_user_feed(username)
    return render_template("user-feed.html", username=username, user_posts=user_posts)


@app.route("/tag/<tagname>")
def post_by_tag(tagname):
    posts = posts_by_tag(tagname)
    return render_template("tag.html", posts=posts, tagname=tagname)


@app.route("/bookmarks/")
def show_bookmarks():
    posts = load_bookmarks()
    return render_template("bookmarks.html", posts=posts)


if __name__ == "__main__":
    app.run()
