from application.interface import UserRepository
from domain.entities import User
from typing import List


class CreateUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self, username: str, email: str) -> User | ValueError:
        user = User(id=None, username=username, email=email, password=None)
        if user.is_valid_email():
            return self.repository.save(user)
        return ValueError("Email is not valid")
    

class ListUserUseCase:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def execute(self) -> List[User]:
        return self.repository.get_all()