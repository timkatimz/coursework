from utils import load_data, get_post, load_comments, show_comments, search_posts, get_user_feed


def test_load_data():
    data = load_data()
    assert type(data) == list, "Возвращается не список"


def test_get_post():
    primary_key = get_post(3)["pk"]
    poster_name = get_post(5)["poster_name"]
    assert primary_key == 3, "Возвращает неправильный primary key"
    assert poster_name == "leo", "Возвращает неправильный poster name"

def test_load_comments():
    comments = load_comments()
    assert comments[0]["commenter_name"] == "hanna", "Возвращает неверное значение"


def test_show_comments():
    comment_list = show_comments(7)
    for comment in comment_list:
        name = comment["commenter_name"]
        post_id = comment["post_id"]
        primary_key = comment["pk"]
    assert name == "hanna"
    assert post_id == 7, "Возвращает неправильный id комментария"
    assert primary_key == 20, "Возвращает неправильный primary key"


def test_search_posts():
    posts = search_posts("лампочка")
    for post in posts:
        name = post["poster_name"]
        views_count = post["views_count"]
        primary_key = post["pk"]
    assert type(posts) == list, "Возвращается не список"
    assert name == "johnny"
    assert views_count == 299, "Возвращает неправильный id комментария"
    assert primary_key == 6, "Возвращает неправильный primary key"


def test_get_user_feed():
    assert type(get_user_feed("leo")) == list, "Возвращает не список"
    assert get_user_feed("leo")[0]["likes_count"] == 154, "Вовращает неправильное количество лайков"