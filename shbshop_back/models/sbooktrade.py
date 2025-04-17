from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .shop import Shop

class Sbooktrade(Base):
    __tablename__ = 'sbooktrade'
    __table_args__ = (
        ForeignKeyConstraint(['sid'], ['shop.sid'], ondelete='CASCADE', onupdate='RESTRICT', name='FK_shop_TO_sbooktrade_1'),
        Index('FK_shop_TO_sbooktrade_1', 'sid')
    )

    bid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    sid: Mapped[int] = mapped_column(BigInteger)
    title: Mapped[str] = mapped_column(String(255))
    author: Mapped[str] = mapped_column(String(255))
    publish: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    detail: Mapped[str] = mapped_column(String(255))
    region: Mapped[str] = mapped_column(String(64))
    img1: Mapped[str] = mapped_column(String(255))
    img2: Mapped[str] = mapped_column(String(255))
    img3: Mapped[str] = mapped_column(String(255))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))

    shop: Mapped['Shop'] = relationship('Shop', back_populates='sbooktrade')