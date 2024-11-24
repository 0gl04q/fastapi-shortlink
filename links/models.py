from datetime import datetime, timedelta

from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from settings.database import Base, int_pk


class Link(Base):
    id: Mapped[int_pk]
    original_url: Mapped[str]
    short_url: Mapped[str]
    slug: Mapped[str]
    expires_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now() + timedelta(days=1))
    click_count: Mapped[int] = mapped_column(default=0)

    click_logs: Mapped[list['ClickLog']] = relationship('ClickLog', back_populates='link')

    def __str__(self):
        return f'{self.__class__.__name__}(original_url={self.original_url}, short_url={self.short_url})'


class ClickLog(Base):
    id: Mapped[int_pk]
    timestamp: Mapped[int]
    user_agent: Mapped[str]
    ip_address: Mapped[str]

    link_id: Mapped[int] = mapped_column(ForeignKey('links.id'), default=1, server_default=text("1"))
    link: Mapped['Link'] = relationship('Link', back_populates='click_logs')

    def __str__(self):
        return f'{self.__class__.__name__}(link={self.link}, ip_address={self.ip_address})'
