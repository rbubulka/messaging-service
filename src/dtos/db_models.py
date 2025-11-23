from sqlalchemy import Enum as SQLEnum, Numeric, String, DateTime, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import datetime
class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = "Messages"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sent_by: Mapped[str] = mapped_column(String(255), nullable = False)
    recieved_by: Mapped[str] = mapped_column(String(255), nullable = False)
    conversation_id: Mapped[int] = mapped_column(Integer, nullable=False)
    date_sent: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True))
    body: Mapped[Text] = mapped_column(Text)
    message_type: Mapped[SQLEnum] = mapped_column(SQLEnum('email','sms','mms',name='message_type',create_type=False))
    attachment: Mapped[Text] = mapped_column(Text, nullable=True)
    provider: Mapped[str] = mapped_column(String, nullable=True)


class Conversation(Base):
    __tablename__ = "Conversations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    member_1: Mapped[str] = mapped_column(String(255), nullable = False)
    member_2: Mapped[str] = mapped_column(String(255), nullable = False)