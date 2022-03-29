import json


def api_posts():
    with open("data/data.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def api_post(post_id):
    for post in api_posts():
        if post_id == post["pk"]:
            return post
