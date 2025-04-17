from typing import Optional, List, TYPE_CHECKING
from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
import datetime

if TYPE_CHECKING:
    from .commercial import Commercial
    from .favorite4c import Favorite4c
    from .favorite4p import Favorite4p
    from .sbooktrade import Sbooktrade

class Shop(Base):
    __tablename__ = 'shop'
    __table_args__ = (
        ForeignKeyConstraint(['cid'], ['commercial.cid'], name='FK_commercial_TO_shop_1'),
        Index('FK_commercial_TO_shop_1', 'cid')
    )

    sid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    cid: Mapped[int] = mapped_column(BigInteger)
    presidentName: Mapped[str] = mapped_column(String(13))
    businessmanName: Mapped[str] = mapped_column(String(13))
    shopName: Mapped[str] = mapped_column(String(255))
    shoptel: Mapped[str] = mapped_column(String(255))
    businessEmail: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))
    region: Mapped[str] = mapped_column(String(64))
    open: Mapped[str] = mapped_column(String(16))
    close: Mapped[str] = mapped_column(String(16))
    holiday: Mapped[str] = mapped_column(String(255))
    shopimg1: Mapped[str] = mapped_column(String(255))
    shopimg2: Mapped[str] = mapped_column(String(255))
    shopimg3: Mapped[str] = mapped_column(String(255))
    etc: Mapped[str] = mapped_column(String(255))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))

    commercial: Mapped['Commercial'] = relationship('Commercial', back_populates='shop')
    favorite4c: Mapped[List['Favorite4c']] = relationship('Favorite4c', back_populates='shop')
    favorite4p: Mapped[List['Favorite4p']] = relationship('Favorite4p', back_populates='shop')
    sbooktrade: Mapped[List['Sbooktrade']] = relationship('Sbooktrade', back_populates='shop')