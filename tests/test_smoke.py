from app.main import hello


def test_hello():
    assert hello("adam") == "hello adam"
