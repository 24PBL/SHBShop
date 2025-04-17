from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .personal import Personal
    from .shop import Shop

class Favorite4p(Base):
    __tablename__ = 'favorite4p'
    __table_args__ = (
        ForeignKeyConstraint(['pid'], ['personal.pid'], name='FK_personal_TO_favorite4p_1'),
        ForeignKeyConstraint(['sid'], ['shop.sid'], name='FK_shop_TO_favorite4p_1'),
        Index('FK_personal_TO_favorite4p_1', 'pid'),
        Index('FK_shop_TO_favorite4p_1', 'sid')
    )

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    pid: Mapped[int] = mapped_column(BigInteger)
    sid: Mapped[int] = mapped_column(BigInteger)

    personal: Mapped['Personal'] = relationship('Personal', back_populates='favorite4p')
    shop: Mapped['Shop'] = relationship('Shop', back_populates='favorite4p')
