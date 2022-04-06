from utils import load_data, get_post, load_comments, show_comments, search_posts, get_user_feed


def test_load_data():
    data = load_data()
    assert type(data) == list, "Возвращается не список"


def test_get_post():
    data = get_post(3)["pk"]
    assert data == 3, "Возвращает неправильное значение"


def test_load_comments():
    comments = load_comments()
    assert comments[0]["commenter_name"] == "hanna", "Возвращает неверное значение"


def test_show_comments():
    comment_list = show_comments(7)
    for i in comment_list:
        name = i["commenter_name"]
        id = i["post_id"]
        pk = i["pk"]
    assert name == "hanna"
    assert id == 7, "Возвращает неправильный id комментария"
    assert pk == 20, "Возвращает неправильный primary key"


def test_search_posts():
    posts = search_posts("а")
    assert type(posts) == list, "Возвращается не список"


def test_get_user_feed():
    assert type(get_user_feed("leo")) == list, "Возвращает не список"
