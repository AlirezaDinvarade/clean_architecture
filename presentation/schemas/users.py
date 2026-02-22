from pydantic import BaseModel, EmailStr


class CreateUserRequest(BaseModel):
    username: str
    password: str
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True  # Allows Pydantic to read from non-dict objects
