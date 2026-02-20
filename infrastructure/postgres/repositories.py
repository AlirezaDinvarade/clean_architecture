from domain.entities import User
from typing import List
from application.interface import UserRepository
from sqlalchemy.orm import Session
from infrastructure.postgres.models import UserModel


class PostgresUserRepository(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session


    def save(self, user: User) -> User:
        db_user = UserModel(usename=user.username, email=user.email)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        user.id = db_user.id
        return user
    
    def get_all(self) -> List[User]:
        db_users = self.session.query(UserModel).all()
        return [
            User(id=u.id, username=u.username, email=u.email, password=u.password)
            for u in db_users
        ]
    
    def get_by_username(self, username: str) -> User:
        return self.session.query(UserModel).filter(UserModel.username == username).first()
