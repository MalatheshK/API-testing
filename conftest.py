import pytest
from utils.api import get


@pytest.fixture(scope="session")
def posts_response():
    return get("/posts")


@pytest.fixture(scope="session")
def posts_data(posts_response):
    return posts_response.json()