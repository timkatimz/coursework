from flask import Flask, request, render_template
from utils import load_data, get_post, show_comments, search_posts, get_user_feed, posts_by_tag
from api.views import api
from bookmarks.views import bookmarks

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
data = load_data()
app.config["BOOKMARKS_PATH"] = "data/bookmarks.json"
app.register_blueprint(api)
app.register_blueprint(bookmarks)


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


@app.route("/tag/<tagname>")
def post_by_tag(tagname):
    posts = posts_by_tag(tagname)
    return render_template("tag.html", posts=posts, tagname=tagname)




if __name__ == "__main__":
    app.run()
