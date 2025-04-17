from typing import List, Optional

from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, text, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

class Base(DeclarativeBase):
    pass


class Adminacc(Base):
    __tablename__ = 'adminacc'

    aid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    acc: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))


class Auth4cfpw(Base):
    __tablename__ = 'auth4cfpw'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


class Auth4cjoin(Base):
    __tablename__ = 'auth4cjoin'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


class Auth4pfpw(Base):
    __tablename__ = 'auth4pfpw'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


class Auth4pjoin(Base):
    __tablename__ = 'auth4pjoin'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


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
    coNumber: Mapped[int] = mapped_column(Integer)
    licence: Mapped[str] = mapped_column(String(255))
    state: Mapped[int] = mapped_column(Integer, server_default=text("'1'"))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    img: Mapped[Optional[str]] = mapped_column(String(255))

    commercialcert: Mapped[List['Commercialcert']] = relationship('Commercialcert', back_populates='commercial')


class Personal(Base):
    __tablename__ = 'personal'

    pid: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    nickname: Mapped[str] = mapped_column(String(64))
    address: Mapped[str] = mapped_column(String(255))
    region: Mapped[str] = mapped_column(String(64))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))
    img: Mapped[Optional[str]] = mapped_column(String(255))


class Vaild4cfpw(Base):
    __tablename__ = 'vaild4cfpw'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


class Vaild4cjoin(Base):
    __tablename__ = 'vaild4cjoin'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


class Vaild4pfpw(Base):
    __tablename__ = 'vaild4pfpw'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


class Vaild4pjoin(Base):
    __tablename__ = 'vaild4pjoin'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    authCode: Mapped[int] = mapped_column(Integer)


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
    coNumber: Mapped[int] = mapped_column(Integer)
    licence: Mapped[str] = mapped_column(String(255))
    reason: Mapped[str] = mapped_column(String(255), server_default=text("'심사중'"))
    state: Mapped[int] = mapped_column(Integer, server_default=text("1"))
    createAt: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=text('CURRENT_TIMESTAMP'))

    commercial: Mapped['Commercial'] = relationship('Commercial', back_populates='commercialcert')
