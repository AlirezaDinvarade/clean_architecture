import secrets
from domain.entities import Token, User
from datetime import timedelta
from application.interface import UserRepository, TokenRepository


class LoginUseCase:
    def __init__(self, user_repo: UserRepository, token_repo: TokenRepository) -> None:
        self.user_repo = user_repo
        self.token_repo = token_repo

    def execute(self, username: str, password: str) -> Token:
        user = self.user_repo.get_by_username(username=username)

        if not user or user.password != password:
            raise ValueError("Invalid username or password")
            
        token = secrets.token_hex(32)
        self.token_repo.save_token(token=token, user_id=user.id, expire_seconds=timedelta(days=1))

        return Token(token=token, user=user)
    
