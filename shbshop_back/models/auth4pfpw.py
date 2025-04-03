from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Auth4pfpw(Base):
    __tablename__ = 'auth4pfpw'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)