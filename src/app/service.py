from typing import Dict, List
from app.domain.user import User


def index_by_email(users: List[User]) -> Dict[str, User]:
    return {u.email: u for u in users}
