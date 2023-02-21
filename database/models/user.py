from sqlalchemy_utils import ChoiceType
from telebot.types import User as TgUser
from typing import Optional

from sqlalchemy import String, Column
from sqlalchemy.orm import Mapped, mapped_column

from const_package.const import EN, RU, UZ
from database.models.base import Base


class User(Base):
    LANGUAGES = (
        (EN, EN),
        (RU, RU),
        (UZ, UZ),
    )

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(String(60))
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[Optional[str]]
    language: Mapped[str] = Column(ChoiceType(LANGUAGES))
    # fullname: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"{self.username} -> {self.tg_id}"

    @property
    def lang(self):
        return self.language.value

    @staticmethod
    def create_from_tg_user(from_user: TgUser):
        return User(
            tg_id=from_user.id,
            username=from_user.username,
            first_name=from_user.first_name,
            last_name=from_user.last_name,
            language=EN,
        )
