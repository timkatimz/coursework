from utils import load_data, get_post, load_comments, show_comments, search_posts, get_user_feed
import pytest


class TestUtils:

    def test_load_data(self):
        data = load_data()
        assert type(data) == list, "Возвращается не список"

    def test_get_post(self):
        assert get_post(3)["pk"] == 3, "Возвращает неправильное значение"

    def test_load_comments(self):
        comments = load_comments()
        assert comments[0]["commenter_name"] == "hanna", "Возвращает неверное значение"

    def test_show_comments(self):
        comment = show_comments(7)
        assert comment["pk"] == 20, "Возвращает не тот комментарий"

    def test_search_posts(self):
        posts = search_posts("а")
        assert type(posts) == list, "Возвращается не список"

    def test_get_user_feed(self):
        assert get_user_feed("leo") == list, "Возвращает не список"
