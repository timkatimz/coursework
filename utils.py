import json


def load_data():
    with open("data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_post(post_id):
    for post in load_data():
        if post_id == post["pk"]:
            return post


def load_comments():
    with open("data/comments.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        return data


def show_comments(post_id):
    comments = []
    for comment in load_comments():
        if post_id == comment["post_id"]:
            comments.append(comment)
    return comments


def search_posts(search_key):
    found_posts = []
    for post in load_data():
        if search_key in post["content"] and len(search_key) > 0:
            found_posts.append(post)
    return found_posts


def get_user_feed(username):
    user_posts = []
    for post in load_data():
        if username == post["poster_name"]:
            user_posts.append(post)
    return user_posts


def posts_by_tag(tagname):
    data = load_data()
    posts = []
    tag = tagname
    for post in data:
        if f"#{tag}" in post["content"]:
            posts.append(post)
    return posts
