from pydantic import BaseModel
from presentation.schemas.users import UserResponse

class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    token: str
    user: UserResponse