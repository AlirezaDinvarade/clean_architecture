from typing import List
from fastapi import APIRouter, Depends
from domain.entities import User
from application.use_case.users import CreateUserUseCase, ListUserUseCase
from presentation.dependencies.users import get_list_user_use_case, get_create_user_use_case
from presentation.schemas.users import CreateUserRequest, UserResponse

router = APIRouter()


@router.post("/users/", response_model=UserResponse)
def create_user(input_data: CreateUserRequest, use_case: CreateUserUseCase = Depends(get_create_user_use_case)):
    return use_case.execute(username=input_data.username, email=input_data.email)


@router.post("/users/", response_model=List[UserResponse])
def list_users(use_case: ListUserUseCase = Depends(get_list_user_use_case)):
    return use_case.execute()
