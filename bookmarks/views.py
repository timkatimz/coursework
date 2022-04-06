import json

from flask import Blueprint

bookmarks = Blueprint("bookmarks", __name__, url_prefix="/bookmarks")


@bookmarks.route("/add/<post_id>")
def add_bookmarks(post_id):
    data = get_post(post_id)
    with open("../data/bookmarks.json", "rw", encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)



@bookmarks.route("/remove/<post_id>")
def remove_bookmarks(post_id):
    pass