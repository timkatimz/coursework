from flask import Blueprint, jsonify
from api.utils import api_posts, api_post

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/posts/")
def get_posts_json():
    all_posts = api_posts()
    return jsonify(all_posts)


@api.route("/posts/<int:post_id>")
def get_select_post(post_id):
    post = api_post(post_id)
    return jsonify(post)
