from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import BigInteger, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
import datetime

if TYPE_CHECKING:
    from .cbooktrade import Cbooktrade
    from .commercial_cert import Commercialcert
    from .shop import Shop
    from .favorite4c import Favorite4c

class Commercial(Base):
    __tablename__ = 'commercial'

    cid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    presidentName: Mapped[str] = mapped_column(String(13))
    businessmanName: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    businessEmail: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    nickname: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(255))
    region: Mapped[str] = mapped_column(String(64))
    coNumber: Mapped[str] = mapped_column(String(255))
    licence: Mapped[str] = mapped_column(String(255))
    state: Mapped[int] = mapped_column(Integer, server_default=text("'1'"))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    img: Mapped[Optional[str]] = mapped_column(String(255))

    cbooktrade: Mapped[List['Cbooktrade']] = relationship('Cbooktrade', back_populates='commercial')
    commercialcert: Mapped[List['Commercialcert']] = relationship('Commercialcert', back_populates='commercial')
    shop: Mapped[List['Shop']] = relationship('Shop', back_populates='commercial')
    favorite4c: Mapped[List['Favorite4c']] = relationship('Favorite4c', back_populates='commercial')