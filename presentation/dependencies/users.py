from sqlalchemy.orm import Session
from application.interface import UserRepository
from application.use_case.users import CreateUserUseCase, ListUserUseCase
from infrastructure.postgres.repositories import PostgresUserRepository
from fastapi import Depends
from database import get_postgres_session


def get_user_repository(session: Session = Depends(get_postgres_session)) -> UserRepository:
    return PostgresUserRepository(session=session)


def get_create_user_use_case(repo: UserRepository = Depends(get_user_repository)):
    return CreateUserUseCase(repository=repo)


def get_list_user_use_case(repo: UserRepository = Depends(get_user_repository)):
    return ListUserUseCase(repository=repo)