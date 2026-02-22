from redis import Redis
from database import get_redis_session
from application.interface import TokenRepository, UserRepository
from fastapi import Depends
from infrastructure.redis.repositories import RedisTokenRepository
from application.use_case.auth import LoginUseCase
from presentation.dependencies.users import get_user_repository


def get_token_repository(session: Redis = Depends(get_redis_session)) -> TokenRepository:
    return RedisTokenRepository(redis_session=session)


def get_login_use_case(token_repo: TokenRepository = Depends(get_token_repository), user_repo: UserRepository = Depends(get_user_repository)) -> LoginUseCase:
    return LoginUseCase(token_repo=token_repo, user_repo=user_repo)