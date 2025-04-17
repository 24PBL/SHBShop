from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .personal import Personal

class Pbooktrade(Base):
    __tablename__ = 'pbooktrade'
    __table_args__ = (
        ForeignKeyConstraint(['pid'], ['personal.pid'], ondelete='CASCADE', onupdate='RESTRICT', name='FK_personal_TO_pbooktrade_1'),
        Index('FK_personal_TO_pbooktrade_1', 'pid')
    )

    bid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    pid: Mapped[int] = mapped_column(BigInteger)
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

    personal: Mapped['Personal'] = relationship('Personal', back_populates='pbooktrade')