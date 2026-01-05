from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    id: int
    email: str
    display_name: Optional[str] = None
