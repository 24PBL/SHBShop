from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Adminacc(Base):
    __tablename__ = 'adminacc'

    aid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    acc: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))