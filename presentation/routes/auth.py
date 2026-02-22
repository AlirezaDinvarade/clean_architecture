from fastapi import APIRouter, Depends
from presentation.schemas.auth import LoginResponse, LoginRequest
from presentation.dependencies.auth import get_login_use_case
from application.use_case.auth import LoginUseCase


router = APIRouter()


@router.post("/login/", response_model=LoginResponse)
def login(input_data: LoginRequest, user_case: LoginUseCase = Depends(get_login_use_case)):
    return user_case.execute(username=input_data.username, password=input_data.password)