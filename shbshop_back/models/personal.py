from typing import Optional
from sqlalchemy import BigInteger, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base
import datetime

class Personal(Base):
    __tablename__ = 'personal'

    pid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    nickname: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(255))
    region: Mapped[str] = mapped_column(String(64))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    img: Mapped[Optional[str]] = mapped_column(String(255))