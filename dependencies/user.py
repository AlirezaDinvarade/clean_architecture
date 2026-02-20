from sqlalchemy.orm import Session
from application.interface import UserRepository
from application.use_case.user import CreateUserUseCase, ListUserUseCase
from infrastructure.postgres.repositories import PostgresUserRepository
from fastapi import Depends
from database import get_db


def get_user_repository(session: Session = Depends(get_db)) -> UserRepository:
    return PostgresUserRepository(session=session)


def get_create_user_use_case(repo: UserRepository = Depends(get_user_repository)):
    return CreateUserUseCase(repository=repo)


def get_list_user_use_case(repo: UserRepository = Depends(get_user_repository)):
    return ListUserUseCase(repository=repo)