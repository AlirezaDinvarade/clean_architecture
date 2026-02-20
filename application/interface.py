from abc import ABC, abstractmethod
from domain.entities import User
from typing import List
from datetime import timedelta


class UserRepository(ABC):

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        pass


class TokenRepository(ABC):

    @abstractmethod
    async def save_token(self, token: str, user_id: int, expire_seconds: timedelta) -> None:
        pass

    @abstractmethod
    async def get_user_id_by_token(self, token: str) -> int | None:
        pass