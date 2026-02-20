from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email: str
    password: str

    def is_valid_email(self) -> bool:
        return "@" in self.email