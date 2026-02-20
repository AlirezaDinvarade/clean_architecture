import pytest
from unittest.mock import MagicMock
from dishka import  Provider, provide, Scope, make_async_container
from application.interface import UserRepository
from application.use_case.user import CreateUserUseCase, ListUserUseCase


class TestUserProvider(Provider):
    def __init__(self):
        super().__init__()
        self.mock_repo = MagicMock()

    @provide(scope=Scope.APP)
    def get_user_repository(self) -> UserRepository:
        return self.mock_repo
    
    @provide(scope=Scope.REQUEST)
    def get_create_user_use_case(self, repo: UserRepository) -> CreateUserUseCase:
        return CreateUserUseCase(repository=repo)
    
    @provide(scope=Scope.REQUEST)
    def get_list_users_use_case(self, repo: UserRepository) -> ListUserUseCase:
        return ListUserUseCase(repository=repo)


@pytest.mark.asyncio
async def test_create_user():
    provider = TestUserProvider()
    container = make_async_container(provider)

    expected_user = {"id": 100, "username": "test_user"}
    provider.mock_repo.save.return_value = expected_user

    async with container() as request_container:
        use_case = await request_container.get(CreateUserUseCase)
        result = use_case.execute("test_user", "test@example.com")

    assert result == expected_user
    


