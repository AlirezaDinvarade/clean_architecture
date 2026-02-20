from typing import List
from fastapi import APIRouter, Depends
from domain.entities import User
from application.use_case.user import CreateUserUseCase, ListUserUseCase
from dependencies.user import get_list_user_use_case, get_create_user_use_case


router = APIRouter()


@router.post("/users/", response_model=User)
def create_user(username: str, email: str, use_case: CreateUserUseCase = Depends(get_create_user_use_case)):
    return use_case.execute(username=username, email=email)


@router.post("/users/", response_model=List[User])
def list_users(use_case: ListUserUseCase = Depends(get_list_user_use_case)):
    return use_case.execute()
