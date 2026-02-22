from application.interface import TokenRepository
from redis import Redis
from datetime import timedelta


class RedisTokenRepository(TokenRepository):
    def __init__(self, redis_session: Redis) -> None:
        self.redis_session = redis_session

    def save_token(self, token: str, user_id: int, expire_seconds: timedelta) -> None:
        self.redis_session.set(f"token:{token}", user_id, ex=expire_seconds)
        return None

    def get_user_id_by_token(self, token: str) -> int | None:
        user_id = self.redis_session.get(f"token:{token}")
        if not user_id:
            ValueError("user not found")
        return user_id