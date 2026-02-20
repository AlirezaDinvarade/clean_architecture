from application.interface import UserRepository
from domain.entities import User
from typing import List


class MemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        self.users: List[User] = []

    def save(self, user: User) -> User:
        user.id = len(self.users) + 1
        print(f"User {user.username} saved to Memory!")
        return user
    
    def get_all(self) -> List[User]:
        return self.users