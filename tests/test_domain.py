from app.domain.user import User
from app.service import index_by_email


def test_index_by_email():
    users = [User(id=1, email="a@x.pl"), User(id=2, email="b@x.pl", display_name="b")]
    idx = index_by_email(users)
    assert idx["a@x.pl"].id == 1
    assert idx["b@x.pl"].display_name == "b"
