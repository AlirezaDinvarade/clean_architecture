from application.interface import TokenRepository
from redis.asyncio import Redis
from datetime import timedelta


class RedisTokenRepository(TokenRepository):
    def __init__(self, redis_client: Redis) -> None:
        self.redis_client = redis_client

    async def save_token(self, token: str, user_id: int, expire_seconds: timedelta) -> None:
        await self.redis_client.set(f"token:{token}", user_id, ex=expire_seconds)

    async def get_user_id_by_token(self, token: str) -> int | None:
        user_id = await self.redis_client.get(f"token:{token}")
        if user_id:
            return int(user_id)
        return None