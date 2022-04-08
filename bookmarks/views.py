from bookmarks.utils import add_bookmark, remove_bookmark
from utils import get_post
from flask import Blueprint, redirect, render_template

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/bookmarks")


@bookmarks.route("/add/<int:post_id>")
def add_bookmarks(post_id):
    post = get_post(post_id)
    add_bookmark(post)
    return redirect("/", code=302)


@bookmarks.route("/remove/<int:post_id>")
def remove_bookmarks(post_id):
    remove_bookmark(post_id)
    return redirect("/", code=302)


