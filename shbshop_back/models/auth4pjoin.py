from sqlalchemy import BigInteger, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Auth4pjoin(Base):
    __tablename__ = 'auth4pjoin'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)