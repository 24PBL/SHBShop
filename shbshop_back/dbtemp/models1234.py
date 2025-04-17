from typing import List, Optional

from sqlalchemy import BigInteger, ForeignKeyConstraint, Index, Integer, String, TIMESTAMP, text
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


class Auth4cur(Base):
    __tablename__ = 'auth4cur'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
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


class Auth4pur(Base):
    __tablename__ = 'auth4pur'

    idx: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(13))
    birth: Mapped[str] = mapped_column(String(10))
    tel: Mapped[str] = mapped_column(String(13))
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
    coNumber: Mapped[str] = mapped_column(String(255))
    licence: Mapped[str] = mapped_column(String(255))
    state: Mapped[int] = mapped_column(Integer, server_default=text("'1'"))
    createAt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    img: Mapped[Optional[str]] = mapped_column(String(255))

    commercialcert: Mapped[List['Commercialcert']] = relationship('Commercialcert', back_populates='commercial')
    shop: Mapped[List['Shop']] = relationship('Shop', back_populates='commercial')
    favorite4c: Mapped[List['Favorite4c']] = relationship('Favorite4c', back_populates='commercial')


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
    createAt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    img: Mapped[Optional[str]] = mapped_column(String(255))

    favorite4p: Mapped[List['Favorite4p']] = relationship('Favorite4p', back_populates='personal')


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


class Vaild4cur(Base):
    __tablename__ = 'vaild4cur'

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


class Vaild4pur(Base):
    __tablename__ = 'vaild4pur'

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
    coNumber: Mapped[str] = mapped_column(String(255))
    licence: Mapped[str] = mapped_column(String(255))
    reason: Mapped[str] = mapped_column(String(255), server_default=text("'심사중'"))
    state: Mapped[int] = mapped_column(Integer, server_default=text("'1'"))
    createAt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    commercial: Mapped['Commercial'] = relationship('Commercial', back_populates='commercialcert')


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
    shoptel: Mapped[str] = mapped_column(String(255))
    businessEmail: Mapped[str] = mapped_column(String(255))
    address: Mapped[str] = mapped_column(String(255))
    open: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    close: Mapped[datetime.datetime] = mapped_column(TIMESTAMP)
    hoilday: Mapped[str] = mapped_column(String(255))
    shopimg1: Mapped[str] = mapped_column(String(255))
    shopimg2: Mapped[str] = mapped_column(String(255))
    shopimg3: Mapped[str] = mapped_column(String(255))
    etc: Mapped[str] = mapped_column(String(255))
    createAt: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

    commercial: Mapped['Commercial'] = relationship('Commercial', back_populates='shop')
    favorite4c: Mapped[List['Favorite4c']] = relationship('Favorite4c', back_populates='shop')
    favorite4p: Mapped[List['Favorite4p']] = relationship('Favorite4p', back_populates='shop')


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
