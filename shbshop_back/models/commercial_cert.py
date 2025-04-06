from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .commercial import Commercial

class Commercialcert(Base):
    __tablename__ = 'commercialcert'
    __table_args__ = (
        ForeignKeyConstraint(['cid'], ['commercial.cid'], name='FK_commercial_TO_commercialcert_1'),
        Index('FK_commercial_TO_commercialcert_1', 'cid')
    )

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    cid: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column(String(13))
    presidentName: Mapped[str] = mapped_column(String(13))
    businessmanName: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    businessEmail: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))
    coNumber: Mapped[str] = mapped_column(String(255))
    licence: Mapped[str] = mapped_column(String(255))
    reason: Mapped[str] = mapped_column(String(255), server_default=text("'심사중'"))
    state: Mapped[int] = mapped_column(Integer, server_default=text("1"))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))

    commercial: Mapped['Commercial'] = relationship('Commercial', back_populates='commercialcert')