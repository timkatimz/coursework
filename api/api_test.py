from main import app


def test_api_posts():
    response = app.test_client().get('/api/posts/')
    assert response.json[0].get('pk') == 1, "Wrong primary key"
    assert response.json[1].get('poster_name') == "johnny", "Wrong poster name"
    assert response.json[1].get('views_count') == 233, "Wrong views count"
    assert type(response.json) == list, "Not a list"


def test_api_posts_by_id():
    response = app.test_client().get("/api/posts/5")
    assert response.json.get('poster_name') == "leo", "Wrong poster name"
    assert response.json.get('pk') == 5, "Wrong primary key"
    assert response.json.get('views_count') == 287, "Wrong views count"
    assert type(response.json) == dict, "Not a list"
