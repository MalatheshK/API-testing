import pytest
from utils.api import get

'''test the schema/structure of the response'''
def test_schema(posts_data):
    for post in posts_data:
        assert "userId" in post
        assert "id" in post
        assert "title" in post
        assert "body" in post

'''test the data type and values of user id'''
def test_user_id(posts_data):
    for post in posts_data:
        assert isinstance(post["userId"], int)
        assert 1 <= post["userId"] <= 10

'''test the value of id is not null'''
def test_id_not_null(posts_data):
    for post in posts_data:
        assert post["id"] is not None

'''test the value of user id is not null'''
def test_user_id_not_null(posts_data):  
    for post in posts_data:
        assert post["userId"] is not None 

'''test the value of title is not empty'''
def test_title_not_empty(posts_data):
    for post in posts_data:
        assert post["title"] != ""

'''test the value of body is not empty'''
def test_body_not_empty(posts_data):
    for post in posts_data:
        assert post["body"] != ""

'''test the value of id is positive and data type is int'''
def test_id_positive(posts_data):
    for post in posts_data:
        assert isinstance(post["id"], int)
        assert post["id"] > 0

'''test the values of id are sequential'''
def test_id_sequential(posts_data):
    ids = [post["id"] for post in posts_data]
    assert ids == list(range(1, 101))

'''test the values of id are unique'''
def test_id_unique(posts_data):
    ids = [post["id"] for post in posts_data]
    assert len(ids) == len(set(ids))

'''test the data type of title is string'''
def test_title_string(posts_data):
    for post in posts_data:
        assert isinstance(post["title"], str)

'''test the data type of body is string'''
def test_body_string(posts_data):
    for post in posts_data:
        assert isinstance(post["body"], str)

'''test the invalid endpoint returns 404'''
def test_invalid_endpoint():
    res = get("/invalid")
    assert res.status_code == 404

'''test the valid post id returns correct data'''
def test_valid_post_id(posts_response):
    res = get("/posts/1")
    assert res.status_code == 200
    post = res.json()
    assert post["id"] == 1
    assert "userId" in post
    assert "title" in post
    assert "body" in post

'''test the invalid post id returns 404 or empty response'''
def test_invalid_post_id():
    res = get("/posts/900")
    assert res.status_code == 404 or res.json() == {}

'''test the valid query parameter'''
def test_query_param(posts_response):
    res = get("/posts?userId=1")
    assert res.status_code == 200
    posts = res.json()
    assert all(post["userId"] == 1 for post in posts)

'''test the invalid query parameter'''
def test_invalid_query_param():
    res = get("/posts?userId=abc")
    assert res.status_code == 200
    assert res.json() == []

'''test the status code of the response'''
def test_status_code(posts_response):
    assert posts_response.status_code == 200

'''test the response time of the API'''
def test_response_time(posts_response):
    assert posts_response.elapsed.total_seconds() < 3
