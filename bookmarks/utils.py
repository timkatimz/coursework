import json


def add_bookmark(post):
    with open("data/bookmarks.json", "r", encoding="utf8") as file:
        data = json.load(file)
        data.append(post)
    with open("data/bookmarks.json", "w", encoding="utf8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)


def remove_bookmark(post_id):
    with open("data/bookmarks.json", "r", encoding="utf8") as file:
        data = json.load(file)
        for post in data:
            if post_id == post["pk"]:
                data.remove(post)
    with open("data/bookmarks.json", "w", encoding="utf8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
