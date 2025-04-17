from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .commercial import Commercial
    from .shop import Shop

class Favorite4c(Base):
    __tablename__ = 'favorite4c'
    __table_args__ = (
        ForeignKeyConstraint(['cid'], ['commercial.cid'], name='FK_commercial_TO_favorite4c_1'),
        ForeignKeyConstraint(['sid'], ['shop.sid'], name='FK_shop_TO_favorite4c_1'),
        Index('FK_commercial_TO_favorite4c_1', 'cid'),
        Index('FK_shop_TO_favorite4c_1', 'sid')
    )

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    sid: Mapped[int] = mapped_column(BigInteger)
    cid: Mapped[int] = mapped_column(BigInteger)

    commercial: Mapped['Commercial'] = relationship('Commercial', back_populates='favorite4c')
    shop: Mapped['Shop'] = relationship('Shop', back_populates='favorite4c')
